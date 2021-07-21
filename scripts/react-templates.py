from copy import deepcopy
from itertools import chain
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory

from typing import Dict, List, Optional

from lxml import html


Components = Dict[str, html.HtmlElement]
Elements = List[html.Element]


def elements_equal(lft: html.HtmlElement, rgt: html.HtmlElement):
    if lft.tag != rgt.tag:
        return False
    if lft.text != rgt.text:
        return False
    if lft.tail != rgt.tail:
        return False
    if lft.attrib != rgt.attrib:
        return False
    if len(lft) != len(lft):
        return False
    return all(elements_equal(l, r) for l, r in zip(lft, rgt))


def component_name(elt: html.HtmlElement) -> Optional[str]:
    prefix = 'component-'
    classes = elt.attrib['class'].split()
    for cls in classes:
        if not cls.startswith(prefix):
            continue
        cls = cls[len(prefix):]
        return ''.join(s.title() for s in cls.split('-'))
    return None


def extract_components(components: Components, header: Elements, filename: Path):
    with open(filename, 'r') as f:
        tree = html.parse(f)

    for elt in chain(tree.xpath('/html/head/*'), tree.xpath('/html/body/script')):
        if any(elements_equal(e, elt) for e in header):
            continue
        header.append(deepcopy(elt))

    for elt in tree.xpath('//*[contains(@class, "component-")]'):
        name = component_name(elt)
        if name is None:
            continue
        if name in components:
            assert elements_equal(elt, components[name])
        else:
            components[name] = deepcopy(elt)


def filter_link_attribute(elt: html.HtmlElement, attrib: str, mode: str = 'js'):
    if attrib not in elt.attrib:
        return
    href = elt.attrib[attrib]
    if not href.startswith('assets/'):
        return
    if mode == 'js':
        elt.attrib[attrib] = f"{{process.env.PUBLIC_URL + '{href}'}}"
    else:
        elt.attrib[attrib] = f'%PUBLIC_URL%/{href}'


def filter_tree(elt: html.HtmlElement, mode: str = 'js'):
    for link in elt.xpath('//a[contains(@class, "react-link")]'):
        link.tag = 'Link'
        if 'class' in link.attrib:
            link.attrib['className'] = link.attrib['class']
            del link.attrib['class']
        link.attrib['to'] = link.attrib['href']
        del link.attrib['href']

    for link in elt.xpath('//link[@rel="stylesheet"]'):
        filter_link_attribute(link, 'href', mode=mode)

    for script in elt.xpath('//script'):
        filter_link_attribute(script, 'src', mode=mode)

    for meta in elt.xpath('//meta[@charset]'):
        meta.attrib['charSet'] = meta.attrib['charset']
        del meta.attrib['charset']


def build_header(elts: Elements, target: Path):
    for elt in elts:
        filter_tree(elt, mode='html')

    with open(target / 'index-template.html', 'r') as f:
        code = f.read()
    code = code.replace('${head}', ''.join(html.tostring(elt).decode() for elt in elts))
    with open(target / 'public' / 'index.html', 'w') as f:
        f.write(code)


def build_component(elt: html.HtmlElement, name: str, target: Path):
    filter_tree(elt)
    fname = f'{name}.rt'
    with TemporaryDirectory() as workpath:
        workpath = Path(workpath)
        with open(workpath / fname, 'wb') as f:
            f.write('<rt-import name="Link" from="react-router-dom" />\n'.encode())
            f.write(html.tostring(elt, method='xml'))
        subprocess.run(['rt', fname, '-f', 'json', '-m', 'es6'], capture_output=True, cwd=workpath).check_returncode()
        shutil.copy(workpath / f'{fname}.js', target / 'src' / 'generated')


def main(src: Path, tgt: Path):
    shutil.rmtree(tgt / 'public' / 'assets')
    shutil.rmtree(tgt / 'src' / 'generated', ignore_errors=True)
    shutil.copytree(src / 'assets', tgt / 'public' / 'assets')
    (tgt / 'src' / 'generated').mkdir()

    components: Components = {}
    header: Elements = []
    for file in src.glob('*.html'):
        extract_components(components, header, file)

    build_header(header, tgt)
    for name, elt in components.items():
        build_component(elt, name, tgt)


if __name__ == '__main__':
    source_path = Path(sys.argv[1])
    target_path = Path(sys.argv[2])
    main(source_path, target_path)

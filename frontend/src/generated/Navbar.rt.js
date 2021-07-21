import * as React from 'react';
import * as _ from 'lodash';
import { Link } from 'react-router-dom';
export default function () {
    return React.createElement('nav', {
        'className': 'navbar navbar-dark navbar-expand-md bg-dark component-navbar',
        'style': { fontFamily: '\'Source Sans Pro\', sans-serif' }
    }, React.createElement('div', { 'className': 'container' }, React.createElement(Link, {
        'className': 'navbar-brand react-link',
        'to': '/'
    }, React.createElement('img', {
        'className': 'logo',
        'src': 'assets/img/logo.svg'
    }), 'FOSIMA'), React.createElement('button', {
        'data-bs-toggle': 'collapse',
        'className': 'navbar-toggler',
        'data-bs-target': '#navcol-1'
    }, React.createElement('span', { 'className': 'visually-hidden' }, 'Toggle navigation'), React.createElement('span', { 'className': 'navbar-toggler-icon' })), React.createElement('div', {
        'className': 'collapse navbar-collapse',
        'id': 'navcol-1'
    }, React.createElement('ul', { 'className': 'navbar-nav flex-grow-1 justify-content-end' }, React.createElement('li', { 'className': 'nav-item' }, React.createElement('a', {
        'className': 'nav-link',
        'href': '#'
    }, 'First Item')), React.createElement('li', { 'className': 'nav-item' }, React.createElement('a', {
        'className': 'nav-link',
        'href': '#'
    }, 'Second Item')), React.createElement('li', { 'className': 'nav-item' }, React.createElement(Link, {
        'className': 'nav-link react-link',
        'to': '/contact'
    }, 'Contact'))))));
}
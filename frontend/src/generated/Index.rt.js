import * as React from 'react';
import * as _ from 'lodash';
import { Link } from 'react-router-dom';
export default function () {
    return React.createElement('div', {
        'className': 'container component-index',
        'style': { fontFamily: '\'Source Sans Pro\', sans-serif' }
    }, React.createElement('h1', {}, 'Heading'), React.createElement('p', {}, 'Hello, I am ', React.createElement('strong', {}, this.props.name), '.'));
}
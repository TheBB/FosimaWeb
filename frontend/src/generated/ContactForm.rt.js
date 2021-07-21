import * as React from 'react';
import * as _ from 'lodash';
import { Link } from 'react-router-dom';
export default function () {
    return React.createElement('section', {
        'className': 'contact-clean component-contact-form',
        'style': { fontFamily: '\'Source Sans Pro\', sans-serif' }
    }, React.createElement('form', {
        'className': 'border rounded',
        'method': 'post'
    }, React.createElement('h2', { 'className': 'text-center' }, 'Contact'), React.createElement('div', { 'className': 'mb-3' }, React.createElement('input', {
        'className': 'border rounded form-control',
        'type': 'text',
        'name': 'name',
        'placeholder': 'Name'
    })), React.createElement('div', { 'className': 'mb-3' }, React.createElement('input', {
        'className': 'border rounded form-control is-invalid',
        'type': 'email',
        'name': 'email',
        'placeholder': 'E-mail address'
    }), React.createElement('small', { 'className': 'form-text text-danger' }, 'Please enter a correct e-mail address.')), React.createElement('div', { 'className': 'mb-3' }, React.createElement('textarea', {
        'className': 'border rounded form-control',
        'name': 'message',
        'placeholder': 'Message',
        'rows': '14'
    })), React.createElement('div', { 'className': 'mb-3' }, React.createElement('button', {
        'className': 'btn btn-primary',
        'type': 'submit'
    }, 'send '))));
}
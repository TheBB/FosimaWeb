import React from 'react';
import ReactDOM from 'react-dom';
import { Helmet } from 'react-helmet';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import indexRT from './generated/Index.rt';
import navbarRT from './generated/Navbar.rt';
import contactFormRT from './generated/ContactForm.rt';

type IndexProps = {
  name: string,
}

class Index extends React.Component<IndexProps> {
  render = indexRT
}

class Navbar extends React.Component {
  render = navbarRT
}

class ContactForm extends React.Component {
  render = contactFormRT
}

ReactDOM.render(
  <React.Fragment>
    <Router>
      <Navbar />
      <Switch>
        <Route exact path="/">
          <Index name="Eivind Fonn" />
        </Route>
        <Route exact path="/contact">
          <ContactForm />
        </Route>
      </Switch>
    </Router>
  </React.Fragment>,
  document.getElementById('root')
);

import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import BigPredictions from './BigPredictions.js';

import { Navbar, Button, Form, Col, Row} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.css';
import { Route, Switch, Router} from 'react-router-dom';

ReactDOM.render(<App />, document.getElementById('root'));


ReactDOM.render(<BigPredictions />, document.getElementById('bigpredictions'));





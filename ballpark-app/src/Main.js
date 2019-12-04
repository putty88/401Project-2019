import React, {Component} from 'react';
import {HarshRouter, NavLink} from 'react-dom';
import './index.css';
import App from './App';
import BigPredictions from './BigPredictions';
import { Navbar, Button, Form} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.css';
import Route from 'react-dom';


class Main extends Component {
    render() {
    return (
        <HarshRouter>
            <div>
                <Navbar bg="dark" variant="dark" sticky="top">
                <Form inline style={{ padding: 10 }}>
                    <Navbar.Brand className="mr-sm-4" to="/App">Ballpark Bookie</Navbar.Brand>
                    <NavLink to="/App"><Button className="mr-sm-4" variant="danger">Home</Button></NavLink>
                    <NavLink to="/BigPredictions"><Button className="mr-sm-4" variant="primary">Big Predictions</Button></NavLink>
                    <Form.Control className="mr-sm-4" type="text" placeholder="Search" />
                    <Button className="mr-sm-4" variant="danger">Search</Button>
                </Form>
                </Navbar>
            </div>
            <div>
              <Route exact="/App" component={App}/>
              <Route path="/BigPredictions" component={BigPredictions}/>
            </div>
        </HarshRouter>
    );
    }
}
export default Main;

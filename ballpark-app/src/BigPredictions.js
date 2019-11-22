// import React from 'react';
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
// import { Navbar, Jumbotron, Button } from 'react-bootstrap';
import Nav from 'react-bootstrap/Nav'
import {BrowserRouter} from 'react-router-dom';
import { Navbar, Jumbotron, Button, Form, Col, Row} from 'react-bootstrap';

class BigPredictions extends Component {
  render() {
    return (
      <div>
        <div>
          <Navbar bg="dark" variant="dark" sticky="top">
            <Form inline style={{ padding: 10 }}>
              <Navbar.Brand href="#home">Ballpark Bookie</Navbar.Brand>
              <Button variant="danger">Home</Button>
              <Button variant="primary">Big Predictions</Button>
              <Form.Control type="text" placeholder="Search" className="mr-sm-4" />
              <Button className=" "variant="danger">Search</Button>
            </Form>
          </Navbar>
        </div>    
        <div>
          <Row>
            <Col md ="3">
              <BrowserRouter>
              <div className="col-lg-9">
                <div>
                  <h2>Schedules</h2></div>
                  <div>
                    <a href="https://www.mlb.com/dbacks/schedule">
                    <h5 className="text-dark"><u>Arizona Diamondbacks</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/braves/schedule">
                    <h5 className="text-dark"><u>Atlanta Braves</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/orioles/schedule">
                    <h5 className="text-dark"><u>Baltimore Orioles</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/redsox/schedule">
                    <h5 className="text-dark"><u>Boston Red Sox</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/whitesox/schedule">
                    <h5 className="text-dark"><u>Chicago White Sox</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/cubs/schedule">
                    <h5 className="text-dark"><u>Chicago Cubs</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/reds/schedule">
                    <h5 className="text-dark"><u>Cincinnati Reds</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/indians/schedule">
                    <h5 className="text-dark"><u>Cleveland Indians</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/rockies/schedule">
                    <h5 className="text-dark"><u>Colorado Rockies</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/tigers/schedule">
                    <h5 className="text-dark"><u>Detroit Tigers</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/astros/schedule">
                    <h5 className="text-dark"><u>Houston Astros</u></h5></a></div>
                  <div className="  ">
                    <a href="https://www.mlb.com/royals/schedule">
                    <h5 className="text-dark"><u>Kansas City Royals</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/angels/schedule">
                    <h5 className="text-dark"><u>Los Angeles Angels</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/dodgers/schedule">
                    <h5 className="text-dark"><u>Los Angeles Dodgers</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/marlins/schedule">
                    <h5 className="text-dark"><u>Miami Marlins</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/brewers/schedule">
                    <h5 className="text-dark"><u>Milwaukee Brewers</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/twins/schedule">
                    <h5 className="text-dark"><u>Minnesota Twins</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/yankees/schedule">
                    <h5 className="text-dark"><u>New York Yankees</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/mets/schedule">
                    <h5 className="text-dark"><u>New York Mets</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/athletics/schedule">
                    <h5 className="text-dark"><u>Oakland Athletics</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/phillies/schedule">
                    <h5 className="text-dark"><u>Philadelphia Phillies</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/pirates/schedule">
                    <h5 className="text-dark"><u>Pittsburgh Pirates</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/padres/schedule">
                    <h5 className="text-dark"><u>San Diego Padres</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/giants/schedule">
                    <h5 className="text-dark"><u>San Fransisco Giants</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/mariners/schedule">
                    <h5 className="text-dark"><u>Seattle Mariners</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/cardinals/schedule">
                    <h5 className="text-dark"><u>St. Louis Cardinals</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/rays/schedule">
                    <h5 className="text-dark"><u>Tampa Bay Rays</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/rangers/schedule">
                    <h5 className="text-dark"><u>Texas Rangers</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/bluejays/schedule">
                    <h5 className="text-dark"><u>Toronto Blue Jays</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/nationals/schedule">
                    <h5 className="text-dark"><u>Washington Nationals</u></h5></a></div>  
              </div>
              </BrowserRouter>
            </Col>
            <Col>
              <div>
                <Row className="justify-content-md-center">
                  <Form>
                    <Form.Group controlId="team1">
                      <Form.Label>Playoff Chances</Form.Label>
                      <Form.Control type="team" placeholder="Enter a team" />
                    </Form.Group>
                  </Form>
                </Row>
                <Row className="justify-content-md-center">
                  <div>
                    <Button  variant="primary" size="sm">
                      Calculate
                    </Button>
                  </div>
                </Row>
              </div>
            </Col>
          </Row>
        </div>
      </div>
    );
  }
}

export default BigPredictions;
// import React from 'react';
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
// import { Navbar, Jumbotron, Button } from 'react-bootstrap';
import Nav from 'react-bootstrap/Nav'
import {BrowserRouter} from 'react-router-dom';
import { Navbar, Jumbotron, Button, Form, Col, Row} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.css';

let CHOSENTEAM

class BigPredictions extends Component {
  constructor(props) {
    super(props)

    this.state = {
      chosenTeam: null,
      ranking: [27, 18, 9, 2, 7, 11, 30, 28, 23, 4, 19, 1, 26, 20, 6, 14, 13, 29, 17, 5, 15, 25, 8, 10, 16, 21, 3, 24, 22, 12],
      result: null,
      text: ''
    }
  }

  submitBigPrediction = event => {
    var chosenTeam = event.target.value;
    console.log(chosenTeam)
    this.setState({
      chosenTeam
    })
  }

  calculateButton = () => {
    this.setState({
      text: 'Playoff Ranking: ' + this.state.ranking[CHOSENTEAM]
    });
  }

  render() {

    const {
      ranking,
      chosenTeam
    } = this.state
    if (chosenTeam != null) {
      CHOSENTEAM = chosenTeam

    }
    

    console.log("BIG PREDICIONS RESULT: ")
    return (
      <div>
        <div>
          <Navbar bg="dark" variant="dark" sticky="top">
            <Form inline style={{ padding: 10 }}>
              <Navbar.Brand className="mr-sm-4" href="#home">Ballpark Bookie</Navbar.Brand>
              <Button className="mr-sm-4" variant="danger">Home</Button>
              <Button className="mr-sm-4" variant="primary">Big Predictions</Button>
              <Form.Control className="mr-sm-4" type="text" placeholder="Search" className="mr-sm-4" />
              <Button className="mr-sm-4" variant="danger">Search</Button>
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
              <div className="col-lg-9 mx-auto">
                <Row>
                  <div>
                    <select as={Col} md="6" className="TeamOne-Select" onChange={this.submitBigPrediction} inline = "true" style={{ padding: 10 }}>
                      <option>Pick One Team</option>
                      <option value="29">Arizona Diamondbacks</option>
                      <option value="19">Atlanta Braves</option>
                      <option value="0">Baltimore Orioles</option>
                      <option value="2">Boston Red Sox</option>
                      <option value="8">Chicago White Sox</option>
                      <option value="20">Chicago Cubs</option>
                      <option value="24">Cincinnati Reds</option>
                      <option value="5">Cleveland Indians</option>
                      <option value="27">Colorado Rockies</option>
                      <option value="6">Detroit Tigers</option>
                      <option value="11">Houston Astros</option>
                      <option value="7">Kansas City Royals</option>
                      <option value="13">Los Angeles Angels</option>
                      <option value="26">Los Angeles Dodgers</option>
                      <option value="17">Miami Marlins</option>
                      <option value="23">Milwaukee Brewers</option>
                      <option value="9">Minnesota Twins</option>
                      <option value="3">New York Yankees</option>
                      <option value="16">New York Mets</option>
                      <option value="14">Oakland Athletics</option>
                      <option value="18">Philadelphia Phillies</option>
                      <option value="21">Pittsburgh Pirates</option>
                      <option value="28">San Diego Padres</option>
                      <option value="25">San Fransisco Giants</option>
                      <option value="12">Seattle Mariners</option>
                      <option value="22">St. Louis Cardinals</option>
                      <option value="4">Tampa Bay Rays</option>
                      <option value="10">Texas Rangers</option>
                      <option value="1">Toronto Blue Jays</option>
                      <option value="15">Washington Nationals</option>
                    </select>
                  </div>
                </Row>
                <Row>
                  <Button variant="primary" type="compare" onClick={this.calculateButton}>
                    Calculate
                  </Button>
                </Row>
                <Row>
                  <h1>{this.state.text}</h1>
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
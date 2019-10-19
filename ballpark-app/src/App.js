// import React from 'react';
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
// import { Navbar, Jumbotron, Button } from 'react-bootstrap';
import Nav from 'react-bootstrap/Nav'
import { Navbar, Jumbotron, Button, Form, Col, Row } from 'react-bootstrap';

// function App() {
//   return (
//     <div classNameName="App">
//       <header classNameName="App-header">
//         <img src={logo} classNameName="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           classNameName="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }
class App extends Component {
  render() {
    return (
      <div>
        <Navbar bg="dark" variant="dark" sticky="top">
          <Form inline style={{ padding: 10 }}>
            <Navbar.Brand href="#home">Ballpark Bookie</Navbar.Brand>
            <Button variant="danger">Home</Button>
            <Button variant="primary">Big Predictions</Button>
            <Form.Control type="text" placeholder="Search" className="mr-sm-2" />
            <Button className=" "variant="danger">Search</Button>
          </Form>
        </Navbar>    
        <div>
          <Row>
            <Col>
              <div className="col-lg-2">
                <div className="pl-3">
                  <h2 className=" pl-3">Schedules</h2></div>
                  <div onclick="window.location.href='https://www.nfl.com/'">
                    <h5 className="text-dark"><u>Arizona Diamondbacks</u></h5></div>
                  <div onclick="window.location.href='https://www.thefantasyfootballers.com'">
                    <h5 className="text-dark"><u>Atlanta Braves</u></h5></div>
                  <div onclick="window.location.href='https://www.fantasypros.com/'">
                    <h5 className="text-dark"><u>Baltimore Orioles</u></h5></div>
                  <div onclick="window.location.href='http://www.espn.com/nfl/'">
                    <h5 className="text-dark"><u>Boston Red Sox</u></h5></div>
                  <div onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>Chicago White Sox</u></h5></div>
                  <div onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>Chicago Cubs</u></h5></div>
                  <div onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>Cincinnati Reds</u></h5></div>
                  <div onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>Cleveland Indians</u></h5></div>
                  <div onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>Colorado Rockies</u></h5></div>
                  <div onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>Detroit Tigers</u></h5></div>
                  <div onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>Houston Astros</u></h5></div>
                  <div className="  " onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>Kansas City Royals</u></h5></div>
                  <div onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>Los Angeles Angels</u></h5></div>
                  <div onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>Los Angeles Dodgers</u></h5></div>
                  <div onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>Miami Marlins</u></h5></div>
                  <div onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>Milwaukee Brewers</u></h5></div>
                  <div onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>Minnesota Twins</u></h5></div>
                  <div onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>New York Yankees</u></h5></div>
                  <div onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>New York Mets</u></h5></div>
                  <div onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>Oakland Athletics</u></h5></div>
                  <div onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>Philadelphia Phillies</u></h5></div>
                  <div onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>Pittsburgh Pirates</u></h5></div>
                  <div onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>San Diego Padres</u></h5></div>
                  <div onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>San Fransisco Giants</u></h5></div>
                  <div onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>Seattle Mariners</u></h5></div>
                  <div onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>St. Louis Cardinals</u></h5></div>
                  <div onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>Tampa Bay Rays</u></h5></div>
                  <div onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>Texas Rangers</u></h5></div>
                  <div onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>Toronto Blue Jays</u></h5></div>
                  <div onclick="window.location.href='https://www.ncaa.com/sports/football/fbs'">
                    <h5 className="text-dark"><u>Washington Nationals</u></h5></div>  
              </div>
            </Col>
            <Col md="auto">
              <div className="col-lg-6">
                <Row>
                  <Form>
                    <Form.Group as={Col} md="4" controlId="team1">
                      <Form.Label>Team One</Form.Label>
                      <Form.Control type="team" placeholder="Enter Team One" />
                    </Form.Group>
                    <Form.Group as={Col} md="4" controlId="team2">                    
                      <Form.Label>Team Two</Form.Label>
                      <Form.Control type="team" placeholder="Enter Team Two" />
                    </Form.Group>
                  </Form>
                </Row>
                <Row>
                  <Button variant="primary" type="compare">
                    Calculate
                  </Button>
                  <Form.Text classNameName="text-muted">
                    Team ____ will win the game.
                  </Form.Text>
                </Row>
              </div>
            </Col>
          </Row>
        </div>
      </div>
    );
  }
}

export default App;
// import React from 'react';
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
// import { Navbar, Jumbotron, Button } from 'react-bootstrap';
import { Navbar, Jumbotron, Button, Form, Col, Row } from 'react-bootstrap';
// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
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
        <Jumbotron>
            <h1>Ballpark Bookie</h1>
            <p>
              <Button
                bsStyle="success"
                bsSize="large"
                href="http://react-bootstrap.github.io/components.html"
                target="_blank">
                View React Bootstrap Docs
              </Button>
            </p>
            <p>
             <Form>
                <Form.Row>
                  <Form.Group as={Col} md="6" controlId="team1">
                    <Form.Label>Team One</Form.Label>
                    <Form.Control type="team" placeholder="Enter Team One" />
                  </Form.Group>
                  <Form.Group as={Col} md="6" controlId="team2">                    
                    <Form.Label>Team Two</Form.Label>
                    <Form.Control type="team" placeholder="Enter Team Two" />
                  </Form.Group>
                  
                </Form.Row>
              </Form>
            </p>

            <p> 
            <div class="mx-auto">
              <Button variant="primary" type="compare">
                Compare
              </Button>
            </div>
            <div className="mx-auto">
              <Form.Text className="text-muted">
                Team ____ will win the game.
              </Form.Text>
              </div>
            </p>
        </Jumbotron>
      </div>
    );
  }
}

export default App;
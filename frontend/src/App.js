import React, { Component } from 'react';
import './App.css';
import Footer from './components/Footer';
import Match from './components/Match';
import Header from './components/Header';

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      match: null,
    };
  }

  matchCallback = (data) => {
    this.setState({match: data})
  }

  render() {
    return (
      <div className='App'>
        <div className="container">
          <Header callback={this.matchCallback}/>
          <Match match={this.state.match}/>
          <Footer/>
        </div>
      </div>
    );
  }
}

export default App;

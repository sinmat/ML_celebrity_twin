import React, { Component } from 'react';
import './App.css';
import Footer from './components/Footer';
import Match from './components/Match';
import Header from './components/Header';
import Image from './components/Image'

class App extends Component {
  render() {
    return (
      <div className='App'>
        <div className="container">
          <Header/>
          <Image/>
          <Match percentage='50'/>
          <Footer/>
        </div>
      </div>
    );
  }
}

export default App;

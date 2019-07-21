import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      data: null,
      isLoading: false,
      error: null,
    };
  }

  componentDidMount() {
    this.setState({ isLoading: true });

    fetch('http://0.0.0.0:5000/data')
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Something went wrong ...');
      }
    })
    .then((data) => {
      this.setState({ data: data, isLoading: false })
    })
    .catch(error => this.setState({ error, isLoading: false }));
  }

  render() {
    const { data, isLoading, error } = this.state;

    if (error) {
      return <p>{error.message}</p>;
    }

    if (isLoading || !data) {
      return <p>Loading ...</p>;
    }

    console.log(data)

    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            {data.result}
          </p>
        </header>
      </div>
    );
  }
}

export default App;

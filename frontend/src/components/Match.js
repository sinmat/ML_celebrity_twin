import React, { Component } from 'react';

class Match extends Component {
  render() {
    return (
        <div className="container">
            <div className="row">
                <div className="col-lg-12 col-md-12 col-sm-12">
                    <div className="alert alert-secondary" role="alert">
                        <h2 className="display-6 ">It's a {this.props.percentage}% match!</h2>
                    </div>
                </div>
            </div>
        </div>
    );
  }
}

export default Match;


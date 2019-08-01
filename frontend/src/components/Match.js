import React, { Component } from 'react';

class Match extends Component {
  loadImage() {

  }

  render() {
    if(!this.props.match) {
        return null
    }

    return (
        <div className='container'>
            {
                this.props.match.knn.matches.map((item, key) =>
                    <div className="row">
                        <div className="col-lg-6 col-md-6 col-sm-12">
                            <div className="jumbotron">
                                <h2 className="display-6">Your Photo</h2>
                                <hr className="my-4"/>
                                <div className="row">
                                    <div className="col-lg-12">
                                        <img src={"http://localhost:5000/"+this.props.match.file_location} alt="Your photo" className="img-fluid" width="100%"/>
                                    </div>
                                </div>    
                            </div>
                        </div>
                        <div className="col-lg-6 col-md-6 col-sm-12">
                            <div className="jumbotron">
                                <h2 className="display-6">Match</h2>
                                <hr className="my-4"/>
                                <div className="row">
                                    <div className="col-lg-12">
                                        <img src={"https://raw.githubusercontent.com/sinmat/ML_celebrity_twin/master/ml/faces/train/"+this.props.match.knn.matches[key].images[0].id+"/"+this.props.match.knn.matches[key].images[0].image} alt="Your photo" className="img-fluid" width="100%"/>
                                    </div>
                                </div>    
                            </div>
                        </div>
                        <div className="col-lg-12 col-md-12 col-sm-12">
                            <div className="alert alert-secondary" role="alert">
                                <h2 className="display-6 ">It's a {(1 - this.props.match.knn.matches[key].distance).toFixed(2)*100}% match!</h2>
                            </div>
                        </div>
                    </div>
                )
            }
        </div>       
    );
  }
}

export default Match;


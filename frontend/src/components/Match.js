import React, { Component } from 'react';
import demoPhoto from '../img/photo.jpg'

class Match extends Component {
  renderPercentage() {
    let response = this.props.match.knn.matches.map(function(item, i) {
        let percentage = (1 - item.distance).toFixed(2)
    })
    return response
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
                        <div className="col-lg-4 col-md-4 col-sm-12">
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
                        <div className="col-lg-4 col-md-4 col-sm-12">
                            <div className="jumbotron">
                                <h2 className="display-6">Encoding Match</h2>
                                <hr className="my-4"/>
                                <div className="row">
                                    <div className="col-lg-12">
                                        <img src={demoPhoto} alt="Your photo" className="img-fluid" width="100%"/>
                                    </div>
                                </div>    
                                <div className="alert alert-secondary" role="alert">
                                    <h2 className="display-6 ">It's a 100% match!</h2>
                                </div>
                            </div>
                        </div>
                        <div className="col-lg-4 col-md-4 col-sm-12">
                            <div className="jumbotron">
                                <h2 className="display-6">Attribute Match</h2>
                                <hr className="my-4"/>
                                <div className="row">
                                    <div className="col-lg-12">
                                        <img src={demoPhoto} alt="Your photo" className="img-fluid" width="100%"/>
                                    </div>
                                </div>    
                            </div>
                        </div>
                    </div>
                    )
                }
            )
        </div>       
    );
  }
}

export default Match;


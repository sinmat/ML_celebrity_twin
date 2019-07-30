import React, { Component } from 'react';
import demoPhoto from '../img/photo.jpg'

class Image extends Component {
  render() {
    let uploadedImg = demoPhoto
    if(this.props.match) {
        uploadedImg = "http://localhost:5000/"+this.props.match.file_location
    }
    return (
        <div className='container'>
            <div className="row">
                <div className="col-lg-6 col-md-6 col-sm-12">
                    <div className="jumbotron">
                        <h2 className="display-6">Encoding Match</h2>
                        <hr className="my-4"/>
                            <div className="row">
                                <div className="col-lg-12">
                                    <img src={demoPhoto} alt="Your photo" className="img-fluid" width="100%"/>
                                </div>
                            </div>    
                    </div>
                </div>
                <div className="col-lg-6 col-md-6 col-sm-12">
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
        </div>       
    );
  }
}



export default Image;
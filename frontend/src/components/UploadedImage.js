import React, { Component } from 'react';
import demoPhoto from '../img/photo.jpg'

class UploadedImage extends Component {

  render() {
      console.log(this.props)
    let uploadedImg = demoPhoto
    if(this.props.match) {
        uploadedImg = "http://localhost:5000/"+this.props.match.file_location
    }
    return (
        <div className='container'>
            <div className="row">
                <div className="col-lg-12 col-md-12 col-sm-12">
                    <div className="jumbotron">
                        <h2 className="display-6">Your Photo</h2>
                        <hr className="my-4"/>
                            <div className="row">
                                <div className="col-lg-12">
                                    <img src={uploadedImg} alt="Your photo" className="img-fluid" width="100%"/>
                                </div>
                            </div>    
                    </div>
                </div>
            </div>
        </div>       
    );
  }
}



export default UploadedImage;
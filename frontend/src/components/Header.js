import React, { Component } from 'react';

class Header extends Component {
  render() {
    return (
        <div className="row">
            <div className="col-lg-12 col-md-12 col-sm-12">
                <div className="jumbotron">
                    <h1 className="display-4">Find Your Celebrity Twin!</h1>
                        <p>Play the game and find your celebrity twin.
                        First model is going to encode 128 dots on your face, match it to celebrity photos and find the best match based on these encodings.
                        Second model will find your best match based on hot-encoding attributes.</p>  
                        <hr className="my-4"></hr>
                        <p className="mb-0">Whenever you're ready upload your photo and wait for the magic to happen!</p>
                        <br/>
                        <button className="btn btn-secondary btn-lg" href="" role="button">Upload photo</button>
                </div>
            </div>
        </div>
               
    );
  }
}



export default Header;



import React, { Component } from 'react';

class Header extends Component {
  onChangeHandler=event=>{
    event.preventDefault();
    const data = new FormData();
    data.append('file', this.uploadInput.files[0]);
    fetch('http://localhost:5000/match', {
      method: 'POST',
      body: data,
    }).then((response) => {
      response.json().then((body) => {
        //console.log(body)
        this.props.callback(body)
      });
    });
  }

  render() {
    return (
        <div className="row">
            <div className="col-lg-12 col-md-12 col-sm-12">
                <div className="jumbotron">
                    <h1 className="display-4">Find Your Celebrity Twin!</h1>
                    <p>Play the game and find your celebrity twin.
                    The face recognition model is going to encode 128 dots on your face, match it to celebrity photos and find the best match based on these encodings.
                    </p>  
                    <hr className="my-4"></hr>
                    <p className="mb-0">Whenever you're ready upload your photo and wait for the magic to happen!</p>
                    <br/>
                    <button className="btn btn-secondary btn-lg upload-btn">
                      Upload photo
                      <input ref={(ref) => { this.uploadInput = ref; }} type="file" onChange={this.onChangeHandler}/>
                    </button>
                </div>
            </div>
        </div>
    );
  }
}



export default Header;



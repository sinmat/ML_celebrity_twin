import React, { Component } from 'react';

class Match extends Component {
  constructor() {
      super()
      this.onClickNext = this.onClickNext.bind(this)
      this.state = {
					matches: []
      }
	}

	// https://medium.com/@gianpaul.r/rendering-new-images-onclick-in-react-7cf0fee2184f
  onClickNext(key) {
		let matches = this.state.matches

		if(matches[key].index < (matches[key].images.length - 1)) {
			matches[key].index += 1
			this.setState({matches: matches})
		} else {
			matches[key].index = 0
			this.setState({matches: matches})
		}
  }
	
  render() {
    if(!this.props.match) {
        return null
		}
		
		this.state.matches = this.props.match.knn.matches

    return (
        <div className='container'>
            {
                this.props.match.knn.matches.map((item, key) =>
                    <div className="row" key={item.match}>
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
																				<img src={"https://raw.githubusercontent.com/sinmat/ML_celebrity_twin/master/ml/faces/train/"+item.match+"/"+item.images[this.state.matches[key].index].image} className="img-fluid" width="100%" onClick={this.onClickNext.bind(this, key)}/>
                                    </div>
                                </div>    
                            </div>
                        </div>
                        <div className="col-lg-12 col-md-12 col-sm-12">
                            <div className="alert alert-secondary" role="alert">
                                <h2 className="display-6 ">It's a {((1-this.props.match.knn.matches[key].distance)*100).toFixed(2)}% match!</h2>
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


import React, {Component} from 'react';
import ReactDOM from 'react-dom';

import './components/main.css'
import User from './user'
import Rating from './Rating'

class App extends Component {
    constructor() {
        super();
        this.handleChange = this.handleChange.bind(this);
    }



    render() {
        return (

            <section className="section">
                    <div className="container-fluid">
                        <div className="columns">
                            <div className="col-sm-3" id="user_col">

                            </div>

                            <div className="col-sm-3" id="rating_col">

                            </div>

                            <div className="col-sm-6">
                                <br/>
                                <h1 className="title is-1 is-1"> Ratings </h1>
                                <hr/>
                                <br/>
                            </div>
                        </div>
                    </div>
            </section>
        );
    }

    handleChange(event) {
        const obj = {};
        obj[event.target.name] = event.target.value;
        this.setState(obj)
    }
}


ReactDOM.render(<App/>, document.getElementById('root'));
ReactDOM.render(<User/>,document.getElementById('user_col'));
ReactDOM.render(<Rating/>,document.getElementById('rating_col'));
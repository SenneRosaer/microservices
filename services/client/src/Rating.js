import React, {Component} from 'react';
import axios from 'axios';
import AddEntity from "./components/AddRatingEntity";


class Rating extends Component {
    constructor() {
        super();

        this.state = {
            id : '',
            type: 'Bus',
            username: '',
            password: ''

        };
        this.addEntity = this.addEntity.bind(this);
        this.handleChange = this.handleChange.bind(this);

    }


    render() {
        return (
            <section className="rating">
                <br/>
                <h1 className="title is-1 is-1"> Actions </h1>
                <hr/>
                <br/>
                <AddEntity addEntity={this.addEntity} id={this.state.id} type={this.state.type}
                           handleChange={this.handleChange}
                           username={this.state.username} password={this.state.password}/>
            </section>
        )
    }

    addEntity(event) {
        event.preventDefault();
        const data = {
            username: this.state.username,
            password: this.state.password,
            id: this.state.id,
            type: this.state.type,
        };
        console.log("??");
        axios.post(`${process.env.REACT_APP_USERS_SERVICE_URL}/rating`,data)
            .then((res) => {
                console.log("reee");
                console.log(res);
                this.setState({username: '', type: 'Bus', id: '', password: ''});
            })
            .catch((err) => {
                console.log(err);
            })


    }
    handleChange(event) {
        const obj = {};
        obj[event.target.name] = event.target.value;
        this.setState(obj)
    }
}

export default Rating
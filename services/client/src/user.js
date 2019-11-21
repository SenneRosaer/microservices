import React, {Component} from 'react';
import axios from 'axios';
import AddUser from "./components/AddUser";


class User extends Component {
    constructor() {
        super();
        this.state = {
            username: '',
            email: '',
            password: '',
        };

        this.addUser = this.addUser.bind(this);
        this.handleChange = this.handleChange.bind(this);

    }


    render() {
        return (
            <section className="user">
                <br/>
                <h1 className="title is-1 is-1"> Register </h1>
                <hr/>
                <br/>
                <AddUser username={this.state.username} email={this.state.email} password={this.state.password}
                         addUser={this.addUser}
                         handleChange={this.handleChange}/>
                <br/>
                <br/>
            </section>
        )
    }

    addUser(event) {
        event.preventDefault();
        const data = {
            username: this.state.username,
            email: this.state.email,
            password: this.state.password,
        };

        axios.post(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`, data)
            .then((res) => {

                this.setState({username: '', email: '', password:''});
                console.log(res);
                if(res['data']['message'] === 'Email already exists'){
                    console.log('Email already exists')
                }
                if(res['data']['message'] === 'Username already exists'){
                    console.log('Username already exists')
                }
            })
            .catch((err) => {
                console.log(err);
            });
    };

    handleChange(event) {
        const obj = {};
        obj[event.target.name] = event.target.value;
        this.setState(obj)
    }
}

export default User
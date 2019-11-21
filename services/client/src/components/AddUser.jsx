import React from 'react'

const AddUser = (props) => {
    return (
        <form onSubmit={(event => props.addUser(event))}>
            <div className="field">
                <input name="username" className="input is-large" type="text" placeholder="Enter a username" value={props.username} required
                    onChange={props.handleChange}
                />
            </div>
            <div className="field">
                <input name="email" className="input is-large" type="email" placeholder="Enter an email address" value={props.email} required
                    onChange={props.handleChange}
                />
            </div>
            <div className="field">
                <input name="password" className="input is-large" type="password" placeholder="Enter a password" value={props.password} required
                    onChange={props.handleChange}
                />
            </div>
            <input type="submit" className="btn btn-primary btn-lg btn-block" value="Submit" />
        </form>
    )
};

export default AddUser;
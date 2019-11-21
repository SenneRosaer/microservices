import React from 'react';

const AddEntity = (props) => {
    return (
        <div className="BusTramContainer">

            <button type="button" className="btn btn-primary btn-lg btn-block" data-toggle="modal"
                    data-target="#AddBusTramModal">
                Add Bus or Tram
            </button>

            <div className="modal fade" id="AddBusTramModal" tabIndex="-1" role="dialog" aria-hidden="true">
                <div className="modal-dialog" role="document">
                    <div className="modal-content">
                        <div className="modal-header">
                            <h4 className="modal-title" id="AddBusTramModal"> Add bus or tram </h4>
                            <button type="button" className="close" data-dismiss="modal" aria-label="Close">
                                <span aria-hidden="true"> &times; </span>
                            </button>
                        </div>
                        <div className="modal-body">
                            <form onSubmit={(event => props.addEntity(event))}>
                                <div className="field">
                                    <input name="id" className="input is-large" type="text" placeholder="Enter an ID"
                                           value={props.id} required onChange={props.handleChange}
                                    />
                                </div>
                                <div className="field">
                                    <select name="type" value={props.type} onChange={props.handleChange}>
                                        <option value="bus">Bus</option>
                                        <option value="tram">Tram</option>
                                    </select>
                                </div>

                                <div className="field">
                                    <input name="username" className="input is-large" type="text"
                                           placeholder="Enter a username" value={props.username} required
                                           onChange={props.handleChange}
                                    />
                                </div>

                                <div className="field">
                                    <input name="password" className="input is-large" type="password"
                                           placeholder="Enter a password" value={props.password} required
                                           onChange={props.handleChange}
                                    />
                                </div>
                                <input type="submit" className="btn btn-primary" value="Submit"/>
                            </form>
                        </div>

                        <div className="modal-footer">
                            <button type="button" className="btn btn-secondary" data-dismiss="modal">Close</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
};

export default AddEntity;

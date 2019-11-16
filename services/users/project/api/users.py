from flask import Blueprint, jsonify, request
from project import db
from project.api.models import User

users_blueprint = Blueprint('users',__name__)

@users_blueprint.route('/', methods=['GET'])
def temporary():
    return jsonify({
        'Hello':'World'
    })


@users_blueprint.route('/users', methods=['POST'])
def add_user():
    post = request.get_json()

    response_for_fail = {
        'status' : 'fail',
        'message' : 'Invalid payload'
    }
    if not post:
        return jsonify(response_for_fail), 400

    #TODO toevoegen voor dubbele data p43 tutorial
    username = post.get('username')
    email = post.get('email')
    password = post.get('password')

    db.session.add(User(username=username,email=email,password=password))
    db.session.commit()
    response = {
        'status' : 'success',
        'message': f'{email} was added'
    }

    return jsonify(response), 201


@users_blueprint.route('/users',methods=['GET'])
def get_all_users():

    response = {
        'status' : 'success',
        'data' : {
            'users' : [user.to_json() for user in User.query.all()]
        }
    }

    return jsonify(response), 200

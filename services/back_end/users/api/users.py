from flask import Blueprint, jsonify, request, render_template
from database.models import db
from database.models import User
from sqlalchemy import exc

users_blueprint = Blueprint('users',__name__,template_folder='./templates')



@users_blueprint.route('/users', methods=['POST'])
def add_user():
    post = request.get_json()

    response_for_fail = {
        'status' : 'fail',
        'message' : 'Invalid payload'
    }
    if not post:
        return jsonify(response_for_fail), 400

    username = post.get('username')
    email = post.get('email')
    password = post.get('password')

    try:
        user = User.query.filter_by(email=email).first()
        if not user:
            user2 = User.query.filter_by(username=username).first()
            if not user2:
                db.session.add(User(username=username,email=email,password=password))
                db.session.commit()
                response = {
                    'status' : 'success',
                    'message': f'{email} was added'
                }

                return jsonify(response), 201
            else:
                return jsonify({
                    'status' : 'fail',
                    'message' : 'Username already exists'
                }) , 201
        else:
            return jsonify({
                'status': 'fail',
                'message': 'Email already exists'
            }), 201
    except exc.IntegrityError as err:
        db.session.rollback()
        return jsonify(response_for_fail),400

@users_blueprint.route('/users',methods=['GET'])
def get_all_users():

    response = {
        'status' : 'success',
        'data' : {
            'users' : [user.to_json() for user in User.query.all()]
        }
    }

    return jsonify(response), 200



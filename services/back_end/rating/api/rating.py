from flask import Blueprint, jsonify, request, render_template
from database.models import db
from database.models import Rating, User
from sqlalchemy import exc

rating_blueprint = Blueprint('rating',__name__)




@rating_blueprint.route('/rating', methods=['POST'])
def add_entity():
    post = request.get_json()

    response_for_fail = {
        'status' : 'fail',
        'message' : 'Invalid payload'
    }
    if not post:
        return jsonify(response_for_fail), 400

    id = post.get('id')
    type = post.get('type')
    username = post.get('username')
    pwd = post.get('password')
    added_by_user = True

    try:
        user = User.query.filter_by(username=username).first()
        if user:
            if user.password == pwd:
                print("succes")
            db.session.add(Rating(id=id,type=type,user=username,added_by_user=added_by_user))
            db.session.commit()
            response = {
                'status' : 'success',
                'message': f'{id} was added'
            }

            return jsonify(response), 201
        else:
            return jsonify({
                'status' : 'fail',
                'message' : 'Username does not exist',
                'user' : user.username
            }) , 201

    except exc.IntegrityError as err:
        db.session.rollback()
        return jsonify(response_for_fail),400



@rating_blueprint.route('/rating',methods=['GET'])
def get_all_ratings():

    response = {
        'status' : 'success',
        'data' : {
            'users' : [rate.to_json() for rate in Rating.query.all()]
        }
    }

    return jsonify(response), 200



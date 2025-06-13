from flask import Blueprint, make_response, request
from models import db, User

user_bp = Blueprint('user_pb', __name__)

@user_bp.route("/<username>")
def username(username):
    return f'Hello {username}'

@user_bp.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        users_list = [user.to_dict() for user in User.query.all()]

        return make_response(users_list, 200)

from app.database.user_parser import parser
from flask import jsonify
from flask_restful import Resource, abort
from app.database.models import User
from app.database import db_session
from app.database.controllers import UserController



class UserResource(Resource):
    def get(self, user_id):
        user = UserController.get_user(user_id)
        if user is None:
            abort(404, message='User not found!')
            return None
        return jsonify(
            {
                'user': user.to_dict(
                    only=(
                        'user_id', 'username', 'password',
                        'basket', 'is_superuser', 'is_active'
                    )
                )
            }
        )


class UserListResource(Resource):
    def post(self):
        user = UserController.create_user()
        return jsonify(
            {
                'user': user.to_dict(
                    only=(
                        'user_id', 'username', 'password',
                        'basket', 'is_superuser', 'is_active'
                    )
                )
            }
        )

class UserResource(Resource):
    def get(self, user_id):
        user = UserController.get_user(user_id)
        if user is None:
            abort(404, message='User not found!')
            return None
        return jsonify(
            {
                'user': user.to_dict(
                    only=(
                        'user_id', 'username', 'password',
                        'basket', 'is_superuser', 'is_active'
                    )
                )
            }
        )
    def post(self):
        users = UserController.get_all_users()
        return jsonify(
            {
                'users': [users.to_dict(
                    only=(
                        'user_id', 'username', 'password',
                        'basket', 'is_superuser', 'is_active'
                    )
                )
                for user in users]
            }
        )
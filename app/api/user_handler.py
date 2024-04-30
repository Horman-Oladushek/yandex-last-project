from app.database.user_parser import parser
from flask import jsonify
from flask_restful import Resource, abort
from app.database.requirements import UserController
from app.database.models import User


class UserResource(Resource):
    def get(self, user_id):
        users = UserController.get_user(user_id)
        return jsonify(
            [{
                'user': user.to_dict(
                    only=(
                        'user_id', 'username', 'password',
                        'basket', 'is_superuser', 'is_active'
                    )
                )
            } for user in users]
        )



class UserListResource(Resource):
    def get(self):
        users = UserController.get_all_users()
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
        args = parser.parse_args()
        user = User(
            username=args['username'],
            password=args['password'],
            basket=args['basket'],
            is_superuser=args['is_superuser'] if args['is_superuser'] is True else False,
            is_active=args['is_active'] if args['is_active'] is True else False
        )
        UserController.create_user(user)
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
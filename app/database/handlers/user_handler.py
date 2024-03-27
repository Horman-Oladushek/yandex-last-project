from app.database.user_parser import parser
from flask import jsonify
from flask_restful import Resource
from app.database.models import User
from app.database import db_session


class ToDoResource(Resource):
    def get(self, todo_id):
        pass
        # todo = get_todo(todo_id)
        # if todo is None:
        #     abort(404, message='Todo not found!')
        #     return None
        # return jsonify(
        #     {
        #         'todo': todo.to_dict(
        #             only=(
        #                 'id', 'title', 'is_finished'
        #             )
        #         )
        #     }
        # )


class ToDoListResource(Resource):
    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            username=args['username'],
            password=args['password'],
            basket=args['basket'],
            is_superuser=args['is_superuser'] if args['is_superuser'] is True else False,
            is_active=args['is_active'] if args['is_active'] is True else False
        )
        session.add(user)
        session.commit()
        return jsonify(
            {
                'users': user.to_dict(
                    only=(
                        'user_id', 'username', 'password',
                        'basket', 'is_superuser', 'is_active'
                    )
                )
            }
        )

from app.database.item_parser import parser
from flask import jsonify
from flask_restful import Resource, abort
from app.database.requirements import ItemController
from app.database.models import Item
from app.database import db_session

class ItemListItems(Resource):
    def post(self):
        args = parser.parse_args()

        item = Item(
            name=args['name'],
            description=args['description'],
            price=args['price'],
            is_sale=args['is_sale'] if args['is_sale'] is True else False,
            discount=args['discount'] if args['is_sale'] is True else "0"
        )
        ItemController.create_item(item)
        return jsonify(
            {
                'item': item.to_dict(
                    only=(
                        'item_id', 'name', 'description',
                        'price', 'is_sale', 'discount'
                    )
                )
            })

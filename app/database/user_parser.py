from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('username', required=True)
parser.add_argument('password', required=True)
parser.add_argument('basket', required=True)
parser.add_argument('is_superuser', required=True)
parser.add_argument('is_active', required=True)
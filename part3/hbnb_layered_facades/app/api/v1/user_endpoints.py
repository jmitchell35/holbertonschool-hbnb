from flask_restx import Namespace, Resource, fields
from app.services import facade
from app.services.exception import (EmailAlreadyExists, InvalidUserData,
                                    UserNotFound)

# Defines /users api route, adds documentation for swagger (description)
api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(
        required=True,
        description='First name of the user'),
    'last_name': fields.String(
        required=True,
        description='Last name of the user'),
    'email': fields.String(
        required=True,
        description='Email of the user'),
    'password': fields.String(
        required=True,
        description='Password of the user')
})

@api.route('/')  # Incomming API call to localhost:5000/users
# Must define all HTTP methods handled by previously defined route (/users)
class UserList(Resource):
    # validates incomming payload / body
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')  # Swagger documentation
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        # Retrieves validated request data / payload / body as dict object
        user_data = api.payload

        try:
            user = facade.user_facade.create_user(user_data)
            return {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
            }, 201
        except EmailAlreadyExists:
            return {'error': 'Email already registered'}, 400
        except InvalidUserData:
            return {'error': 'Invalid input data'}, 400

    @api.response(200, 'Users list retrieved successfully')
    def get(self):
        """Retrieve list of users"""
        return facade.user_facade.get_all_users()

@api.route('/<user_id>')
# user_id comes from route, not payload / body
@api.doc(params={'user_id': 'The user ID'})
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        try:
            user = facade.user_facade.get(user_id)
            return {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
                }, 200
        except UserNotFound:
            return {'error': 'User not found'}, 404

    @api.expect(user_model, validate=True)
    @api.response(200, 'User details updated successfully')
    @api.response(404, 'User not found')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def put(self, user_id):
        """Update one user details"""
        try:
            user = facade.user_facade.get(user_id)
            uptd_user = facade.user_facade.update_user(user, api.payload)
            return {
                'id': uptd_user.id,
                'first_name': uptd_user.first_name,
                'last_name': uptd_user.last_name,
                'email': uptd_user.email
                }, 200
        except UserNotFound:
            return {'error': 'User not found'}, 404
        except EmailAlreadyExists:
            return {'error': 'Email already registered'}, 400
        except InvalidUserData:
            return {'error': 'Invalid input data'}, 400

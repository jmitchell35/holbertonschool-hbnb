from flask_restx import Namespace, Resource, fields
from app.services import facade

# Defines /users api route, adds documentation for swagger (description)
api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(
        required=True, description='First name of the user'),
    'last_name': fields.String(
        required=True, description='Last name of the user'),
    'email': fields.String(
        required=True, description='Email of the user')
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

        # Simulate email uniqueness check (to be replaced by real validation with persistence)
        return facade.users.create_user(user_data)
        if existing_user:
            return {'error': 'Email already registered'}, 400

        new_user = facade.create_user(user_data)
        return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email}, 201
from flask_restx import Namespace, Resource, fields
from app.services import facade
from app.services.exception import (InvalidPlaceData, OwnerNotFound,
                                    PlaceNotFound, AmenityNotFound)

api = Namespace('places', description='Place operations')

place_input_model = api.model('Place', {
    'title': fields.String(
        required=True, description='Title of the place'),
    'description': fields.String(
        description='Description of the place'),
    'price': fields.Float(
        required=True, description='Price per night'),
    'latitude': fields.Float(
        required=True, description='Latitude of the place'),
    'longitude': fields.Float(
        required=True, description='Longitude of the place'),
    'owner_id': fields.String(
        required=True, description='ID of the owner'),
})

review_output_model = api.model('PlaceReview', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Text of the review'),
    'rating': fields.Integer(description='Rating of the place (1-5)'),
    'user_id': fields.String(description='ID of the user')
})

amenity_output_model = api.model('Amenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(required=True, description='Name of the amenity')
})

user_output_model = api.model('User', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(
        required=True, description='First name of the user'),
    'last_name': fields.String(
        required=True, description='Last name of the user'),
    'email': fields.String(
        required=True, description='Email of the user')
})

place_output_model = api.model('Place', {
    'id': fields.String(description='Place ID'),
    'title': fields.String(
        required=True, description='Title of the place'),
    'description': fields.String(
        description='Description of the place'),
    'price': fields.Float(
        required=True, description='Price per night'),
    'latitude': fields.Float(
        required=True, description='Latitude of the place'),
    'longitude': fields.Float(
        required=True, description='Longitude of the place'),
    'owner_id': fields.String(
        required=True, description='ID of the owner'),
    'owner': fields.Nested(user_output_model, description='Owner of the place'),
    'amenities': fields.List(fields.Nested(amenity_output_model), description='List of amenities'),
    'reviews': fields.List(fields.Nested(review_output_model), description='List of reviews')
})

@api.route('/')
class PlaceList(Resource):

    @api.expect(place_input_model, validate=True)
    @api.marshal_with(place_input_model, code=201)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Create a new place"""
        place_data = api.payload

        try:
            place = facade.place_manager.create_place(place_data)
            return place, 201
        except InvalidPlaceData:
            return {'error': 'Invalid input data'}, 400
        except OwnerNotFound:
            return {'error': 'Owner not found'}, 404

    @api.response(200, 'List of places retrieved successfully')
    @api.marshal_list_with(place_output_model)
    def get(self):
        """Retrieve a list of all places"""
        list_of_places = facade.place_facade.get_all_places()
        return list_of_places

@api.route('/<place_id>')
@api.doc(params={'place_id': 'The place ID'})
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        try:
            place = facade.place_manager.get_place_details(place_id)
            return {
                'id': place.get('id'),
                'title': place.get('title'),
                'description': place.get('description'),
                'latitude': place.get('latitude'),
                'longitude': place.get('longitude'),
                'owner': place.get('owner'),
                'amenities': place.get('amenities')
            }
        except PlaceNotFound:
            return {'error': 'Place not found'}, 404
        except OwnerNotFound:
            return {'error': 'Owner not found'}, 404
        except AmenityNotFound:
            return {'error': 'Amenity not found'}, 404
    
    @api.expect(place_input_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        try:
            facade.place_manager.update_place(place_id, api.payload)
            return {
                "message": "Place updated successfully"
            }, 200
        except PlaceNotFound:
            return {'error': 'Place not found'}, 404
        except InvalidPlaceData:
            return {'error': 'Invalid input data'}, 400
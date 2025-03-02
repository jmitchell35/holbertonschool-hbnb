from flask import Flask, jsonify
from flask_restx import Api

def create_app():
    app = Flask(__name__)
    api = Api(
        app,
        version='1.0',
        title='HBnB API',
        description='HBnB Application API',
        doc='/api/v1/'
    )
    
    from app.api.v1.user_endpoints import api as users_ns
    api.add_namespace(users_ns, path='/users')
    from app.api.v1.place_endpoints import api as places_ns
    api.add_namespace(places_ns, path='/places')
    from app.api.v1.amenity_endpoints import api as amenities_ns
    api.add_namespace(amenities_ns, path='/amenities')

    return app
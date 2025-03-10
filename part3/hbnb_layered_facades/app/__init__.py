from flask import Flask, jsonify
from flask_restx import Api
from config import DevelopmentConfig
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

jwt = JWTManager()

bcrypt = Bcrypt()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    api = Api(
        app,
        version='1.0',
        title='HBnB API',
        description='HBnB Application API',
        doc='/api/v1/',
        prefix='/api/v1/'
    )
    
    from app.api.v1.user_endpoints import api as users_ns
    api.add_namespace(users_ns, path='/users')
    from app.api.v1.place_endpoints import api as places_ns
    api.add_namespace(places_ns, path='/places')
    from app.api.v1.amenity_endpoints import api as amenities_ns
    api.add_namespace(amenities_ns, path='/amenities')
    from app.api.v1.review_endpoints import api as review_ns
    api.add_namespace(review_ns, path='/reviews')
    from app.api.v1.auth import api as auth_ns
    api.add_namespace(auth_ns, path='/login')

    bcrypt.init_app(app)

    jwt.init_app(app)

    return app
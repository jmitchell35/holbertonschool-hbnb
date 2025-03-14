from functools import wraps  # Create homemade decorators (wrapper functions)
from flask_jwt_extended import get_jwt, verify_jwt_in_request
from flask_jwt_extended.exceptions import NoAuthorizationError
from flask import request
from app.services import facade
from app.services.exception import UnauthorizedAccess

def admin_required(f):  # custom decorator name, f is decorated function
    @wraps(f)  # below function is executed when above decorator is used
    # *args is for undefined number of iterable arguments (list, tuple...)
    # **args is for undefined number of key-value pairs
    # Basically comes down to enriched variadic functions from C, OOP way.
    def decorated(*args, **kwargs):
        try:
            verify_jwt_in_request()  # performs token check
            jwt_data = get_jwt()
            # False if key is missing, or value is True
            if not jwt_data.get('is_admin', False):
                return {'error': 'Admin privileges required'}, 403
            # Wrapper has done its job, now calls decorated function
            return f(*args, **kwargs)
        except NoAuthorizationError:
            return {"msg": "Missing Authorization Header"}, 401
    return decorated

# PUT user
# Triple-nested because we want to consider the user_id from the request URI
def user_matches_or_admin(func=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Manually verify the JWT
            verify_jwt_in_request()  # performs token check
            jwt_data = get_jwt()
            token_user_id = jwt_data.get('sub')  # logged user

            # Get user_id from Flask's request object
            user_id = request.view_args.get('user_id')

            # get request data
            request_data = request.get_json()

            # Check permissions
            if not (token_user_id == user_id or jwt_data['is_admin']):
                    return {'error': 'Unauthorized action'}, 403

            # Check for unallowed modification
            if not jwt_data['is_admin'] and\
                ('password' in request_data.keys() or\
                    'email' in request_data.keys()):
                    return {'error': 'You cannot modify email or password'}, 400

            return func(*args, **kwargs)
        return wrapper
        
    # This allows the decorator to be used both with and without parentheses
    if func:
        # @user_matches_or_admin (no parentheses)
        return decorator(func)
    else:
        # @user_matches_or_admin() (with parentheses)
        return decorator

# PUT / DELETE place
def owner_matches_or_admin(func=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Manually verify the JWT
            try:
                verify_jwt_in_request()  # performs token check
                jwt_data = get_jwt()
                token_user_id = jwt_data.get('sub')  # logged user

                # Get user_id from Flask's request object
                place_id = request.view_args.get('place_id')
                
                place = facade.place_facade.gateway.get(place_id)

                # Check permissions
                if not (jwt_data.get('is_admin') or\
                        token_user_id == place.owner_id):
                    return {'error': 'Unauthorized action'}, 403

                return func(*args, **kwargs)
            except NoAuthorizationError:
                return {"msg": "Missing Authorization Header"}, 401
        return wrapper

    # This allows the decorator to be used both with and without parentheses
    if func:
        # @user_matches_or_admin (no parentheses)
        return decorator(func)
    else:
        # @user_matches_or_admin() (with parentheses)
        return decorator

# PUT / DELETE review
def is_author(func=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Manually verify the JWT
            verify_jwt_in_request()  # performs token check
            jwt_data = get_jwt()
            token_user_id = jwt_data.get('sub')  # logged user

            # Get user_id from Flask's request object
            review_id = request.view_args.get('review_id')

            requesting_user = facade.user_facade.gateway.get(token_user_id)

            # Check permissions
            if not (jwt_data.get('is_admin') or\
                review_id in requesting_user.reviews):
                return {'error': 'Unauthorized action'}, 403

            return func(*args, **kwargs)
        return wrapper

    # This allows the decorator to be used both with and without parentheses
    if func:
        # @user_matches_or_admin (no parentheses)
        return decorator(func)
    else:
        # @user_matches_or_admin() (with parentheses)
        return decorator

# POST Review
def not_owner_first_review(func=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Manually verify the JWT
            verify_jwt_in_request()  # performs token check
            jwt_data = get_jwt()
            token_user_id = jwt_data.get('sub')  # logged user

            # Get place_id from Flask's request object body
            place_id = (request.get_json()).get('place_id')
            
            requesting_user = facade.user_facade.get(token_user_id)

            # Check permissions
            if place_id in requesting_user.places:
                return {'error': 'You cannot review your own place'}, 400
            
            place = facade.place_facade.get(place_id)
            for review in place.reviews:
                if review in requesting_user.reviews:
                    return {
                        'error': 'You have already reviewed this place'}, 400

            return func(*args, **kwargs)
        return wrapper

    # This allows the decorator to be used both with and without parentheses
    if func:
        # @user_matches_or_admin (no parentheses)
        return decorator(func)
    else:
        # @user_matches_or_admin() (with parentheses)
        return decorator

# POST place
def place_owner_matches_user(func=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Manually verify the JWT
            verify_jwt_in_request()  # performs token check
            jwt_data = get_jwt()
            token_user_id = jwt_data.get('sub')  # logged user

            # Get place_id from Flask's request object body
            owner_id = (request.get_json()).get('owner_id')

            # Check permissions
            if token_user_id != owner_id:
                return {'error': 'Unauthorized action'}, 403

            return func(*args, **kwargs)
        return wrapper

    # This allows the decorator to be used both with and without parentheses
    if func:
        # @user_matches_or_admin (no parentheses)
        return decorator(func)
    else:
        # @user_matches_or_admin() (with parentheses)
        return decorator
class UserError(Exception):
    """Base exception for user-related errors"""
    pass

class EmailAlreadyExists(UserError):
    """Raised when attempting to register with an existing email"""
    pass

class InvalidUserData(UserError):
    """Raised when user data is invalid"""
    pass

class InvalidAmenityData(Exception):
    """Raised when amenity data is invalid."""
    pass

class AmenityAlreadyExists(Exception):
    """Raised when attempting to register an existing amenity"""

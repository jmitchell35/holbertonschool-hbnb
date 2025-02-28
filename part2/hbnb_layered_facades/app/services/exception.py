class UserError(Exception):
    """Base exception for user-related errors"""
    pass

class EmailAlreadyExists(UserError):
    """Raised when attempting to register with an existing email"""
    pass

class InvalidUserData(UserError):
    """Raised when user data is invalid"""
    pass

class UserNotFound(UserError):
    """Raised when user is not found in storage"""
    pass
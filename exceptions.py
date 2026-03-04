class InvalidAdhar(Exception):
    """Raised when the provided Aadhar number does not match records."""
    pass

class InvalidMobileNumber(Exception):
    """Raised when the provided mobile number does not match records."""
    pass

class InCorrectPin(Exception):
    """Raised when the entered PIN is incorrect or does not match."""
    pass

class InvalidAmount(Exception):
    """Raised when the transaction amount is below the minimum or above the limit."""
    pass

class InsufficentFunds(Exception):
    """Raised when the account balance is lower than the requested withdrawal/transfer amount."""
    pass
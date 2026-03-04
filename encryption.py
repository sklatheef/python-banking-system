import hashlib

def encrypt(pin):
    """
    Converts a plain text PIN into a SHA-256 hash.
    Note: In your functions, pin is often passed as an int, 
    so we convert it to a string before hashing.
    """
    pin_str = str(pin)

    return hashlib.sha256(pin_str.encode()).hexdigest()
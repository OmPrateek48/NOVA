import hashlib
import os

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(input_password, stored_hash):
    return hash_password(input_password) == stored_hash

def validate_api_key(api_key):
    valid_keys = os.getenv("VALID_API_KEYS", "").split(",")
    return api_key in valid_keys

if __name__ == "__main__":
    print("SecurityManager loaded.")

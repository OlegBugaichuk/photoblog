import hashlib
import uuid

def hash_password(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password, password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + password.encode()).hexdigest()
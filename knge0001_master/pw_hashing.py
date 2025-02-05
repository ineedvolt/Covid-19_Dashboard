import hashlib


def make_hashes(password):  # password hashing
    return hashlib.sha256(str.encode(password)).hexdigest()


def check_hashes(password, hashed_text):  # check the password
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

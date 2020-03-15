import hashlib


def text_to_hash(string):
    hash_object = hashlib.md5(string.encode())
    return hash_object.hexdigest()

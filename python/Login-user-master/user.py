import hashlib


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self._hash_password(password)
        self.is_logged_in = False

    def _hash_password(self, password):
        hash256 = hashlib.sha256()
        hash256.update(password.encode('utf-8'))
        return hash256.hexdigest()

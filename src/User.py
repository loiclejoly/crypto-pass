from Cipher import AESCipher
import json


class User:
    def __init__(self):
        self.user = None
        self.pwd = None
        self.filename = None
        self.cipher = None
        self.content = None

    def new_account(self, user, pwd, custom_file=None):
        self.cipher = AESCipher(user, pwd)
        self.content = '{"username":"' + user + '", "accounts":{}}'

        if custom_file:
            self.filename = custom_file
        else:
            self.filename = "account_" + user

        encrypted = self.cipher.encrypt(self.content)

        with open(self.filename, 'wb') as f:
            f.write(encrypted)

    def existing_account(self, user, pwd, custom_file=None):
        self.user = user
        self.pwd = pwd
        self.cipher = AESCipher(user, pwd)

        if custom_file:
            self.filename = custom_file
        else:
            self.filename = "account_" + user

        with open(self.filename, 'rb') as f:
            data = f.read()

        self.content = json.loads(self.cipher.decrypt(data))
        print(self.content)

    def get_cipher(self):
        return self.cipher

    def get_filename(self):
        return self.filename

    def update_content(self, new_content):
        self.content = new_content

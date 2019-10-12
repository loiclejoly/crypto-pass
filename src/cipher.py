import base64
import hashlib

from Crypto import Random
from Crypto.Cipher import AES

BS = 16  # Block size


def _padding(string):
    """text + the hexadecimal shift added to have a 16 blocksize multiple"""
    return string + (BS - len(string) % BS) * chr(BS - len(string) % BS)


def _unpadding(string):
    """remove the padding added where string[-1] is the hexadecimal code transformed in integer"""
    return string[0: -string[-1]]


class AESCipher:

    def __init__(self, user, key):
        key = user + key
        self.key = hashlib.sha256(key.encode('utf-8')).digest()

    def encrypt(self, raw):
        raw = _padding(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return _unpadding(cipher.decrypt(enc[16:]))

from Crypto.Cipher import AES
import base64
import os
from config import encryption_key


def encryption(data):
    '''This is for Encryption.It encrypts the data(password) and returns it'''
    BLOCK_SIZE = 16
    PADDING = '{'

    def pad(s): return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

    def EncodeAES(c, s): return base64.b64encode(c.encrypt(pad(s)))
    cipher = AES.new(encryption_key)
    return EncodeAES(cipher, data)


def decryption(data):
    '''This is for Decryption.It decrypts the data(password) and returns it'''
    PADDING = '{'

    def DecodeAES(c, e): return c.decrypt(base64.b64decode(e)).rstrip(PADDING)
    cipher = AES.new(encryption_key)
    return DecodeAES(cipher, data)


if __name__ == '__main__':
    pass

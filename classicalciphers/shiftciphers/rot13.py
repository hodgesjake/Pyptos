"""
ROT13 Cipher

Jake Hodges
"""

from classicalciphers.shiftciphers.caesarcipher import CaesarCipher

class Rot13(CaesarCipher):
    def __init__(self, encrypted_msg=None, decrypted_msg=None, alpha=None, shift=13):
        super().__init__(encrypted_msg, decrypted_msg, alpha, shift)
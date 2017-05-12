"""
ROT13 Cipher

Jake Hodges
"""

from classicalciphers.caesarcipher import CaesarCipher

class Rot13(CaesarCipher):
    def __init__(self, encrypted_msg=None, decrypted_msg=None, alpha=None):
        super().__init__(encrypted_msg, decrypted_msg, alpha, shift=13)

def main():
    rot=Rot13(None,"ABC")
    rot.encrypt()
    print(rot)

#main()
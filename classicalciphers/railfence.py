"""
Rail-fence

Jake Hodges
"""

from classicalciphers.classicalcipher import ClassicalCipher

class RailFence(ClassicalCipher):
    def __init__(self, encrypted_msg=None, decrypted_msg=None, alpha=None, key=0):
        self.key=key
        super().__init__(encrypted_msg,decrypted_msg,alpha)

    def encrypt(self):
        e_msg=""


def main():

text





main()
"""
Standard Shift Cipher

Jake Hodges
"""

from classicalciphers.classicalcipher import ClassicalCipher

#TODO: Capitalization and punctuation
class CaesarCipher(ClassicalCipher):
    def __init__(self, encrypted_msg=None, decrypted_msg=None, alpha=None, shift=0):
        self.shift = shift
        super().__init__(encrypted_msg, decrypted_msg, alpha)

    def encrypt(self):
        e_msg=""
        shift_alpha=self._shift_alpha()
        for char in self.decrypted_msg:
            indx = self.alpha.find(char)
            e_msg+=shift_alpha[indx]
        self.encrypted_msg=e_msg

    def decrypt(self):
        d_msg=""
        shift_alpha=self._shift_alpha()
        for char in self.encrypted_msg:
            indx = self.alpha.find(char)
            d_msg+=shift_alpha[indx]

        self.decrypted_msg=d_msg

    def _shift_alpha(self):
        left = self.alpha[0:self.shift]
        right = self.alpha[self.shift:len(self.alpha)]
        shift_alpha = right+left
        return shift_alpha

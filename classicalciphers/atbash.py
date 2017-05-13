"""
Encrypts and Decrypts Atbash Ciphers

Jake Hodges
"""
from classicalciphers.classicalcipher import ClassicalCipher

class AtbashCipher(ClassicalCipher):
    def __init__(self, encrypted_msg=None, decrypted_msg=None, alpha=None):
        super().__init__(encrypted_msg, decrypted_msg, alpha)

    def decrypt(self):
        rev_key = self._reverse_alpha()
        d_msg = ""
        for char in self.encrypted_msg:
            indx = self.alpha.find(char)
            d_msg += rev_key[indx]
        self.decrypted_msg = d_msg

    def encrypt(self):
        rev_key = self._reverse_alpha()
        e_msg = ""
        for char in self.decrypted_msg:
            indx = self.alpha.find(char)
            e_msg += rev_key[indx]
        self.encrypted_msg = e_msg

    def _reverse_alpha(self):
        reverse_alpha=""
        for i in range(len(self.alpha)-1, -1, -1):
            reverse_alpha += self.alpha[i]
        return reverse_alpha

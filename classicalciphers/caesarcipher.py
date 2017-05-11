"""
Caesar Cipher

Jake Hodges
"""

from classicalciphers.affinecipher import AffineCipher

class CaesarCipher(AffineCipher):
    def __init__(self, encrypted_msg=None, decrypted_msg=None, alpha=None, shift=0):
        super().__init__(encrypted_msg, decrypted_msg, alpha, shift, a=1)

    def encrypt(self):
        super().encrypt()

    def decrypt(self):
        d_msg=""
        shift_alpha=self._shift_alpha()
        for char in self.encrypted_msg:
            indx = self.alpha.find(char)
            d_msg+=shift_alpha[indx]

        self.decrypted_msg=d_msg


def main():
    cc=CaesarCipher(None,"ABC",None,30)
    cc.encrypt()
    print(cc)

#main()
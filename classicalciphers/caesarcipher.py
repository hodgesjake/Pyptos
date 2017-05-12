"""
Caesar Cipher

Jake Hodges
"""

from classicalciphers.affinecipher import AffineCipher

class CaesarCipher(AffineCipher):
    def __init__(self, encrypted_msg=None, decrypted_msg=None, alpha=None, shift=0):
        super().__init__(encrypted_msg, decrypted_msg, alpha, shift, a=1)

def main():
    cc=CaesarCipher("BCDEF",None,None,27)
    cc.decrypt()
    print(cc)

main()
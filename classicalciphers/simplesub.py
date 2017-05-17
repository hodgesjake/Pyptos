"""
Simple Substitution Cipher

Jake Hodges
"""
from classicalciphers.classicalcipher import ClassicalCipher
class SimpleSub(ClassicalCipher):
    def __init__(self,encrypted_msg=None,decrypted_msg=None,alpha=None,key=None):
        self.key=key
        super().__init__(encrypted_msg,decrypted_msg,alpha)

    def encrypt(self):
        e_msg = ""
        for char in self.decrypted_msg:
            indx = self.alpha.find(char)
            e_msg+=self.key[indx]
        self.encrypted_msg = e_msg

    def decrypt(self):
        d_msg = ""
        for char in self.encrypted_msg:
            indx = self.alpha.find(char)
            d_msg += self.key[indx]
        self.decrypted_msg = d_msg

def main():
    ss=SimpleSub("ZYXW",None,None,"ZYXWVUTSRQPONMLKJIHGFEDCBA")
    ss.decrypt()
    print(ss)
main()
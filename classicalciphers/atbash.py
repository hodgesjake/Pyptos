"""
Encrypts and Decrypts Atbash Ciphers

Jake Hodges
"""
from classicciphers.classiccipher import ClassicCipher as CC

#TODO: Be able to use different keys
class AtbashCipher:

    def __init__(self, e_msg=None, d_msg=None):
        self.key = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
        self.e_msg = e_msg
        self.d_msg = d_msg

    def __str__(self):
        return "Atbash:\nENCIPHERED: " + self.e_msg+ "\nDECIPHERED: " + self.d_msg

    def encipher(self):
        e=""
        for char in self.d_msg:
            if char.isalpha():
                indx=CC().alpha_to_index(char)
                new_char=self.key[indx]
            else:
                new_char = char
            e+=new_char
        self.e_msg=e

    def decipher(self):
        d = ""
        for char in self.e_msg:
            if char.isalpha():
                indx = CC().alpha_to_index(char)
                new_char = self.key[indx]
            else:
                new_char = char
            d += new_char
        self.d_msg = d

def _main():

    e = "I am jake."
    atbash_e = AtbashCipher(None, e)
    atbash_e.encipher()
    print(atbash_e)

    d = "r zn qzpv....."
    atbash_d=AtbashCipher(d,None)
    atbash_d.decipher()
    print(atbash_d)




_main()
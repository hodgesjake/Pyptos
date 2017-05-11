"""
Affine Cipher

Jake Hodges
"""

from classicalciphers.classicalcipher import ClassicalCipher
from math import gcd as py_gcd
from random import randint

class AffineCipher(ClassicalCipher):
    def __init__(self, encrypted_msg, decrypted_msg, alpha=None, shift=0, a=None):
        super().__init__(encrypted_msg, decrypted_msg, alpha)
        if a == None:
            self._generate_a()
        else:
            self.a=a

        self.shift = shift

    def _generate_a(self):
        a_list=[]
        for num in range(len(self.alpha)):
            is_coprime = py_gcd(num,len(self.alpha))==1
            if is_coprime:
                a_list.append(num)

        rand_indx = randint(0,len(a_list)-1)
        self.a = a_list[rand_indx]

    def encrypt(self):
        e_msg=""
        for char in self.decrypted_msg:
            indx = self.alpha.find(char)
            new_indx= (self.a * indx + self.shift) % len(self.alpha)
            e_msg+=self.alpha[new_indx]
        self.encrypted_msg = e_msg

    def decrypt(self):



def main():
    aff=AffineCipher(None,"CIPHER", None, 8, None)
    aff.encrypt()
    print(aff)

#main()
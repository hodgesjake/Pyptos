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

        if decrypted_msg==None:
            if a == None:
                self.a = self._pick_a()
            else:
                self.a=a

        else: self.a=a

        self.shift = shift

    def _generate_a_list(self):
        print("genlist")
        a_list=[]
        for num in range(len(self.alpha)):
            is_coprime = py_gcd(num,len(self.alpha))==1
            if is_coprime:
                a_list.append(num)
        return a_list

    def _pick_a(self):
        a_list = self._generate_a_list()
        rand_indx = randint(0, len(a_list) - 1)
        return a_list[rand_indx]

    def encrypt(self):
        e_msg=""
        for char in self.decrypted_msg:
            indx = self.alpha.find(char)
            new_indx= (self.a * indx + self.shift) % len(self.alpha)
            e_msg+=self.alpha[new_indx]
        self.encrypted_msg = e_msg

    def decrypt(self):
        mod_inv= self._modinv(self.a,len(self.alpha))
        d_msg=""
        for char in self.encrypted_msg:
            indx = self.alpha.find(char)
            new_indx=(mod_inv*(indx-self.shift)%len(self.alpha))
            d_msg+=self.alpha[new_indx]

        self.decrypted_msg = d_msg


    def _egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self._egcd(b % a, a)
            return (g, x - (b // a) * y, y)


    def _modinv(self, a, m):
        g, x, y = self._egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

def main():
    aff=AffineCipher("IHHWVCSWFRCP",None,None,8,5)
    aff.decrypt()
    print(aff)
#main()
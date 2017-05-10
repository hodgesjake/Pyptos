"""
Jake Hodges
"""

from classicalciphers.classicalcipher import ClassicalCipher

class ShiftCipher(ClassicalCipher):
    def __init__(self, encrypted_msg=None, decrypted_msg=None, alpha=None, shift=0):
        self.shift = shift
        super().__init__(encrypted_msg, decrypted_msg, alpha)

    def encrypt(self):
        pass

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

###TEST###
shift = ShiftCipher("NOPQRSTUVWXYZABCDEFGHIJKLM", None, None, 13)
shift.decrypt()
print(shift)

"""
Encrypts and Decrypts Atbash Ciphers

Jake Hodges
"""
from classicalciphers.classicalcipher import ClassicalCipher

class AtbashCipher(ClassicalCipher):
    def __init__(self, encrypted_msg=None, decrypted_msg=None, key=None):

        if key==None:
            self.key="ZYXWVUTSRQPONMLKJIHGFEDCBA"
        else:
            self.key=key
        super().__init__(encrypted_msg, decrypted_msg)

    def __str__(self):
        return "ENCRYPTED: " + self.encrypted_msg + "\nDECRYPTED: " + self.decrypted_msg

    def decrypt(self):
        rev_key = self._reverse_key()
        d_msg = ""
        for char in self.encrypted_msg:
            indx = self.key.find(char)
            d_msg += rev_key[indx]
        self.decrypted_msg = d_msg

    def encrypt(self):
        rev_key = self._reverse_key()
        e_msg = ""
        for char in self.decrypted_msg:
            indx = self.key.find(char)
            e_msg += rev_key[indx]
        self.encrypted_msg = e_msg

    def _reverse_key(self):
        reverse_key=""
        for i in range(len(self.key)-1, -1, -1):
            reverse_key += self.key[i]
        return reverse_key


abc = AtbashCipher("ZYX")
abc.decrypt()
print(abc)
print()

speckey = AtbashCipher("987", None, "123456789")
speckey.decrypt()
print(speckey)
print()

encr = AtbashCipher(None, "ABC")
encr.encrypt()
print(encr)
print()

speckey = AtbashCipher(None, "123", "987654321")
speckey.encrypt()
print(speckey)
print()

weirdkey = AtbashCipher("{4le07y7jqwec8v76", None, "qwertyuiop{}asdfghjkl;'zxcvbnm,.,/789456123")
weirdkey.decrypt()
print(weirdkey)
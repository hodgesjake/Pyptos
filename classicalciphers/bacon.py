"""
Bacon Cipher:
This Bacon Cipher makes every character have its own value
e.g. no shared values

Jake Hodges
"""

from classicalciphers.classicalcipher import ClassicalCipher

class BaconCipherV2(ClassicalCipher):
    def __init__(self, encrypted_msg=None, decrypted_msg=None, alpha=None, key="01", key_length=5):
        self.key = "01"
        self.key_length = key_length
        super().__init__(encrypted_msg,decrypted_msg,alpha)

    def encrypt(self):
        e_msg=""
        char_dict=self._create_dict()
        for char in self.decrypted_msg:
            e_msg+=char_dict[char]

        self.encrypted_msg=e_msg



    def decrypt(self):
        pass

    def _create_dict(self):
        bc_dict={}
        for i in range(len(self.alpha)):
            bin_str=bin(i)[2:]
            bin_fix = self._bin_size(bin_str,self.key_length)
            bc_dict[self.alpha[i]]=bin_fix

        return bc_dict

    def _bin_size(self,bin_str,bin_size):
        bin_ret=bin_str
        while len(bin_ret)!=bin_size:
            bin_ret = "0" + bin_ret

        return bin_ret

    """
    This could be used for encrypting with the original key
    """
    def _replace_vals(self,dictionary):
        if self.key!=[0,1]:
            for char in self.alpha:
                val = dictionary[char]
                new_val=""
                for num in val:
                    if num=="0":
                        new_val+=self.key[0]
                    else:
                        new_val+=self.key[1]
                dictionary[char]=new_val
        return dictionary

def main():
    bc=BaconCipherV2(None,"ABC")
    bc.encrypt()
    print(bc)

main()
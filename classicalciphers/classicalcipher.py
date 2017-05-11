"""
Jake Hodges
"""


class ClassicalCipher(object):

    def __init__(self, encrypted_msg=None, decrypted_msg=None, alpha=None):
        self.encrypted_msg=encrypted_msg
        self.decrypted_msg=decrypted_msg
        if alpha==None:
            self.alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        else:
            self.alpha = alpha

    def __str__(self):
        return "ENCRYPTED: " + self.encrypted_msg + "\nDECRYPTED: " + self.decrypted_msg

    def encrypt(self):
        raise NotImplementedError()
    def decrypt(self):
        raise NotImplementedError()



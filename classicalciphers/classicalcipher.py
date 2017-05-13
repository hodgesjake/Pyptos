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
        if self.encrypted_msg==None and self.decrypted_msg==None:
            return "ENCRYPTED: not encrypted" + "\nDECRYPTED: not decrypted"
        elif self.encrypted_msg==None:
            return "ENCRYPTED: not encrypted" + "\nDECRYPTED: " + self.decrypted_msg
        elif self.decrypted_msg==None:
            return "ENCRYPTED: " + self.encrypted_msg + "\nDECRYPTED: not decrypted"
        else:
            return "ENCRYPTED: " + self.encrypted_msg + "\nDECRYPTED: " + self.decrypted_msg

    def encrypt(self):
        raise NotImplementedError()
    def decrypt(self):
        raise NotImplementedError()



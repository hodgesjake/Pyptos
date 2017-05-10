"""
Jake Hodges
"""


class ClassicalCipher(object):

    def __init__(self, encrypted_msg=None, decrypted_msg=None):
        self.encrypted_msg=encrypted_msg
        self.decrypted_msg=decrypted_msg
        #self.alg_type=alg_type
        #self.key=key

    def encrypt(self):
        raise NotImplementedError()
    def decrypt(self):
        raise NotImplementedError()



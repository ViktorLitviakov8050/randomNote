from cryptography.fernet import Fernet

class Cryptographer:
    def __init__(self, key):
        self.cryptosuit  = Fernet(key)

    def encrypt(self, password) -> str:
        password = password.encode()
        cipherpass = self.cryptosuit.encrypt(password)
        return cipherpass
    
    def decrypt(self, encrypted_pass) -> str:
        decrypted_text = self.cryptosuit.decrypt(encrypted_pass).decode()
        return decrypted_text
 
        
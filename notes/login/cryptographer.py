from cryptography.fernet import Fernet

class Cryptographer:
    def __init__(self, key):
        print(key)
        self.cryptosuite  = Fernet(key)

    def encrypt(self, password) -> bytes:
        password = password.encode()
        cipherpass = self.cryptosuite.encrypt(password)
        return cipherpass
    
    def decrypt(self, encrypted_pass) -> str:
        decrypted_text = self.cryptosuite.decrypt(encrypted_pass).decode()
        return decrypted_text
 
        
from cryptography.fernet import Fernet

class Cryptographer:
    def __init__(self, key):
        self.cryptosuite = Fernet(key)

    def encrypt(self, password) -> bytes:
        encoded_password = password.encode()
        encrypted_password = self.cryptosuite.encrypt(encoded_password)
        decoded_password = encrypted_password.decode()

        return decoded_password
    
    def decrypt(self, encrypted_pass) -> str:
        decrypted_password = self.cryptosuite.decrypt(encrypted_pass)
        decoded_password = decrypted_password.decode()

        return decoded_password
 
        
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes




def validate_aes_cbc_encrypt(key, iv, plaintext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    if len(plaintext) % 16 != 0:
        plaintext += b'\x00' * (16 - len(plaintext) % 16)
    return cipher.encrypt(plaintext)

def aes_cbc_encrypt(key, iv, plaintext):
    

def main():
    pass

if __name__ == "__main__":
    main()

import base64
from Crypto.Cipher import AES

def decrypt_aes(x,y):
    cipher = AES.new(y, AES.MODE_ECB)
    plaintext  = cipher.decrypt(x)
    return plaintext

def main():
 with open('7.txt') as text :
    ciphertext = base64.b64decode(text.read())
 key = b'YELLOW SUBMARINE'
 main_text = decrypt_aes(ciphertext , key) 
 print(main_text)  


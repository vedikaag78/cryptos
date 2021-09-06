from base64 import b64encode
str1 = input("enter the string")

encoded_data = b64encode(bytes.fromhex(str1)).decode()


print("Encoded text with base 64 is:", encoded_data)

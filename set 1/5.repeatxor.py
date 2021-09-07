def en_xor(x , k ,y):
   encrpted = []
   for i in range(0, len(x)):
       encrpted.append(x[i] ^ k[i % y])
   return bytes(encrpted)
  
def main():
    s = input("Enter the string: ").encode()
    key = b"ICE"
    key_lenth = len(key)
    print("THe encrypted text: " , en_xor(s,key,key_lenth).hex())
    

if __name__ == "__main__":
    main()
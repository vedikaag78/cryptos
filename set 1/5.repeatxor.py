def en_xor(x , k ,y):
   text = x
   encrpted = []
   for i in range(0, len(x)):
       encrpted.append(text[i] ^ k[i % y])
   return bytes(encrpted)
  




def main():
    s = input(b"The text:")
    key = b"ICE"
    key_lenth = len(key)
    print("THe encrypted text:" , en_xor(s,key,key_lenth).hex())
    

if __name__ == '__main__ ':
    main()
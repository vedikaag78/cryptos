def xor_bytes( input1 , input2):
    bytes_xord = b''
    for x1, x2 in zip(input1 , input2):
        bytes_xord += (bytes([ x1 ^ x2]))
    return bytes_xord  

def main():
    s1 = input("string 1 :")
    s2 = input("string 2 :")
    bytes_s1 = bytes.fromhex(s1)
    bytes_s2 = bytes.fromhex(s2)
    print(xor_bytes(bytes_s1, bytes_s2).hex()) 

# if __name__ == '__main__':
main()
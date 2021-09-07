def single_xor(x,y):
    xord_text = b''
    for a in x:
        xord_text += bytes([a ^ y])
    return xord_text    

def main():
    s = input("Enter the hex code:")
    s = bytes.fromhex(s)
    for i in range(256):
        text = single_xor(s,i)
        print(text)

if __name__ == "__main__":
    main()

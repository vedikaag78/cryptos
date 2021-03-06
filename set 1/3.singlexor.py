def single_xor(x,y):
    xord_text = b''
    for a in x:
        xord_text += bytes([a ^ y])
    return xord_text 

def score_by(input_text):
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }

    return sum([character_frequencies.get(chr(itext) ,0) for itext in input_text.lower() ])

def main():
    s = input("Enter the hex code:")
    s = bytes.fromhex(s)
    all_text = []
    for i in range(256):
        text = single_xor(s,i)
        score = score_by(text)
        data = {
          'text': text,
          'score': score,
          'key': i
        }
        all_text.append(data)
    result = sorted(all_text, key = lambda x : x['score'],reverse= True)[0]
    for ans in result:
        print(result[ans])

if __name__ == "__main__":
    main()

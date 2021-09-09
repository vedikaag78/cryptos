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




def rev_xord(text_b):
    right_text = []
    for key in range(0,256):
        mess = single_xor(text_b,key)
        score = score_by(mess)
        data = {
          'message': mess,
          'score': score,
          'key': key
        }
    right_text.append(data)
    return sorted(right_text, key = lambda x : x['score'],reverse= True)[0]


def main():
    text = open('4.txt').read().splitlines()
    all_text= []
    for i in text:
     text_byte = bytes.fromhex(i)
     all_text.append(rev_xord(text_byte))
    result = sorted(all_text, key = lambda x: x['score'], reverse= True)[0]
    for r in result:
     print(result[r])   

if __name__ == '__main__':
    main()    

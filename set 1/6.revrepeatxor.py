import base64

def cal_distance(a, b):
    hamming_distance = 0
    for b1, b2 in zip(a, b):
        xor = b1 ^ b2
        hamming_distance += sum([1 for bit in bin(xor) if bit == '1'])
    return hamming_distance

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

def bruteforce_sxor(s):
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
   return  sorted(all_text, key = lambda x : x['score'],reverse= True)[0]

def break_xor(x):
    avg_distances = []
    for keys in range(2,41):
        distances = []
        chunks = [x[i:i+keys] for i in range(0, len(x), keys)]
        while True:
            try:
                ch_1 = chunks[0]
                ch_2 = chunks[1]
                hmming_distance = cal_distance(ch_1,ch_2)
                distances.append(hmming_distance/keys)
                del chunks[0]
                del chunks[1]

            except Exception as e:
                  break      
        result = {
            'key': keys,
            'average_distance': sum(distances)/len(distances)
        }
        avg_distances.append(result)
    possible_key_lengths = sorted(avg_distances , key = lambda x:x['average_distance'])[0]
    possible_text = []
    keyz = b''
    possible_key_length = possible_key_lengths['key']
    for i in range(possible_key_length):
      block = b''
      for j in range(0,len(x), possible_key_length):
        block += bytes([x[j]])
      keyz += bytes([bruteforce_sxor(block)['key']]) 
    possible_text.append((repeating_key_xor(x,keyz), keyz)) 
    return max(possible_text, key=lambda x: score_by(x[0]))





def repeating_key_xor(message_bytes, key):
    """Returns message XOR'd with a key. If the message, is longer
    than the key, the key will repeat.
    """
    output_bytes = b''
    index = 0
    for byte in message_bytes:
        output_bytes += bytes([byte ^ key[index]])
        if (index + 1) == len(key):
            index = 0
        else:
            index += 1
    return output_bytes





def main():
    with open('6.txt') as input_file:
        ciphertext = base64.b64decode(input_file.read())
    result, key = break__xor(ciphertext)
    print("Key: {}\nMessage: {}".format(key, result))


if __name__ == '__main__':
    main()
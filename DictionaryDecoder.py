#File for decoding encoder input using DictionaryIverse from DictionaryCreator.py and output of DictionaryEncoder.py
#File is run with: python3 DictionaryDecoder.py <Encoder Output> <DictionaryInverse> <Output File (Optional)> 
#Decoded text is written to file and standard output
import sys  
import binascii

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

filein = open(str(sys.argv[1]),'r')
inputLines = filein.readlines()
filein = open(str(sys.argv[2]),'r')
DictionaryInverse = filein.readlines()

newline = ''
for line in inputLines:
    if (line[0]=='1'): #Decodes line
        recur = int(line[1:4],2)
        str1index = int(line[4:10],2)
        str2index = int(line[10:16],2)
        try:
            str1 = text_from_bits(DictionaryInverse[str1index])
            str2 = text_from_bits(DictionaryInverse[str2index])
            entry = (str1+str2)*recur
            newline+=entry
        except:
            print(str(str1index) + ' ' + str(str2index))
    else:   #Line was not encoded
        char1 = line[0:8]
        char2 = line[8:16]
        newline+=text_from_bits(char1)
        newline+=text_from_bits(char2)
print(newline)        
try:
    fileout = open(str(sys.argv[3]),'w')
except:
    fileout = open('text.out','w')
fileout.write(newline)

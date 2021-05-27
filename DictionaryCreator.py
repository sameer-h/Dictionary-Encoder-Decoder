#File for generating a Dictionary and Dictionary Inverse for common 2-byte patterns in a given text file
#File is run with: python3 DictionaryDecoder.py <Input Text> <Dictionary name (optional)> <Dictionary Inverse name (optional)>
#Dictionary and Inverse are written to files
import sys  
import binascii

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def make16Bit(value):
    leadingzeros=16-len(value)
    for j in range(leadingzeros):
        value='0'+value
    return value

filein = open(str(sys.argv[1]),'r')
filelines = filein.readlines()

Dictionary = []
Recursions = []
for line in filelines: #Find common patterns and how often they appear
    line = line.strip()
    for i in range(0,len(line),2):
        if (line[i:i+2] in Dictionary):
            Recursions[Dictionary.index(line[i:i+2])] += 1
        else:
            Dictionary.append(line[i:i+2])
            Recursions.append(1)


NewDictionary = ['0000000000000000'] * 32768
DictionaryInverse = ['0000000000000000'] * 64
for i in range(1,64):
    if not Dictionary: #Quits if Dictionary is empty before 64 entries are added
        break
    common = max(Recursions) #if pattern only happens once, don't bother adding to the dictionary (Encoding saves no bytes)
    if common == 1:
        break
    entryIndex = Recursions.index(common)
    entry = Dictionary[entryIndex]
    value = text_to_bits(entry)
    NewDictionary[int(value, 2)] = make16Bit(bin(i)[2:])
    DictionaryInverse[i] = value
    del Dictionary[entryIndex]
    del Recursions[entryIndex]

try:
    MyFile = open(str(sys.argv[2]),'w')
except:
    MyFile=open('Dictionary.hack','w')

for element in NewDictionary:
     MyFile.write(element)
     MyFile.write('\n')
MyFile.close()

try:
    MyFile = open(str(sys.argv[3]),'w')
except:
    MyFile=open('DictionaryInv.hack','w')

for element in DictionaryInverse:
     MyFile.write(element)
     MyFile.write('\n')
MyFile.close()
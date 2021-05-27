#File for encoding input using Dictionary from DictionaryCreator.py
#File is run with: python3 DictionaryEncoder.py <Text Input> <Dictionary> <Output File (optional)>
#Old size -> new size written to standard output

import sys  
import binascii

filein = open(str(sys.argv[1]),'r')
inputLines = filein.readlines()
filein = open(str(sys.argv[2]),'r')
Dictionary = filein.readlines()

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def make16Bit(value):
    leadingzeros=16-len(value)
    for j in range(leadingzeros):
        value='0'+value
    return value

def makeXBit(value,X):
    leadingzeros=X-len(value)
    for j in range(leadingzeros):
        value='0'+value
    return value


Output = ""
for line in inputLines:
    line = line.strip()
    line = line.replace('\n',"")
    counter = 1
    prevarg1 = ''
    prevarg2 = ''
    for i in range(0,len(line),4):
        e1 = 0
        if (line[i:i+2] != ''):
            e1 = int(text_to_bits(line[i:i+2]),2)
        e2 = 0
        arg1 = Dictionary[e1]
        arg1 = arg1.replace("\n",'')
        if (line[i+2:i+4] != ''):
            e2 = int(text_to_bits(line[i+2:i+4]),2)
        arg2 = Dictionary[e2]
        arg2 = arg2.replace("\n",'')
        if (line[i:i+2] == '' or line[i+2:i+4] == ''):
            countBin = makeXBit(bin(counter)[2:],3)
            newline = '1' + countBin + prevarg1[-6:] + prevarg2[-6:]
            Output+=newline+"\n"
            counter = 1
    
        if (arg1!="0000000000000000") and arg2!="0000000000000000":
            if (prevarg1 == arg1 and prevarg2 == arg2): #Counts recurrences of a bitstring. Can recur up to 6 times (111)
                counter += 1
                if (counter == 7):
                    countBin = makeXBit(bin(counter)[2:],3)
                    newline = '1' + countBin + prevarg1[-6:] + prevarg2[-6:]
                    if(len(newline)==16):
                        Output+=newline+"\n"
                    counter = 1
                    prevarg1 = ''
                    prevarg2 = ''
            else:
                if (prevarg1 != '' and prevarg2 != ''):
                    countBin = makeXBit(bin(counter)[2:],3)
                    newline = '1' + countBin + prevarg1[-6:] + prevarg2[-6:]
                    if(len(newline)==16):
                        Output+=newline+"\n"
                    counter = 1
                prevarg1 = arg1
                prevarg2 = arg2    
        else:
            countBin = makeXBit(bin(counter)[2:],3)
            newline = '1' + countBin + prevarg1[-6:] + prevarg2[-6:]
            if(e1!=0 and e2!=0 and len(newline)==16):
                Output+=newline+"\n"
            counter = 1
            prevarg1 = ''
            prevarg2 = ''
            if (e1!=0):
                if(len(text_to_bits(line[i:i+2]))==16):
                    Output+=text_to_bits(line[i:i+2])+'\n'#+' '+line[i:i+2]+"\n"
            if (e2!=0):
                if(len(text_to_bits(line[i+2:i+4]))==16):
                    Output+=text_to_bits(line[i+2:i+4])+'\n'#+' '+line[i+2:i+4]+'\n'
print(Output)
try:
    fileout = open(str(sys.argv[3]),'w')
except:
    fileout = open('EncoderOutput.out','w')
fileout.write(Output)

cntchar = 0
for line in inputLines:
    cntchar+=len(line.replace('\n',''))

cntcharout = len(Output.replace('\n','')) // 8

print("Input Size " + str(cntchar) + 'B -> Output Size '+ str(cntcharout)+'B') 



# Dictionary Encoder and Decoder
Computers often store data using a compression algorithm to save space in memory. In this project, I implemented a hardware-based method of encoding and decoding data using dictionaries.

Download the description docx file in this repo to see the full explanation on the project and its implementation.


## Overview ##
- In this project I used HDL, a specialized computer language used to program electronic and digital logic circuits. This allows me to build the actual chips.
- I also used Python to create the actual dictionary and interact with it as so:
``` python
import sys  
import binascii

...

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
            
```

I also have a similar .py file for running the actual Encode and Decode operations based on the HDL.

I often have to convert from ASCII to binary so I created functions in Python:
``` python
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def make16Bit(value):
    leadingzeros=16-len(value)
    for j in range(leadingzeros):
        value='0'+value
    return value
```
These take input and convert it to what their function name suggests.

Next, I'll explain the HDL I wrote for the actual logic behind the project.


### Build all of the chips in the list below ###

Chip Name | File Name | Description
| :---: | :---: | :---:
DictionaryEncoder  | DictionaryEncoder.hdl | Encodes input using dictionary
DictionaryDecoder  | DictionaryDecoder.hdl | Decodes encoded input using dictionary
Eq4 and Eq16       | Eq4.hdl , Eq16.hdl    | Checks equality of input bits

## How Things Work ## 
### 1. Dictionary Encoder is a chip with 3 Inputs: Recur[3], InA[16], and InB[16] ###
  -  Recur stores encoded value for how many times input pattern is repeated. Value ranges from 0-7.
  - InA stores the first 16-bit pattern to be encoded.
  - InB stores the first 16-bit pattern to be encoded.

- Dictionary is loaded into both Rom32k Chips, and the address value for each is set to InA and InB respectively.
- If either rom32K returns a 0 (default), this means encoding has failed, and output will be set to InA.
- If both encodes are successful, output will be stored as:
  #### 1010101110101011 #### 

Where:
- out[15] (Blue) stores a 1 if encoding was successful, 0 if not
- out[12..14] (Red) Stores the number of pattern repetitions, in this case, 2
- out[6..11] (Green) Stores the encoded value of InA
- out[6..11] (Purple) Stores the encoded value of InB

### 2.	DictionaryDecoder: ###
- Design a chip with 1 16-bit input.
  - If In[15] = 1, signal is encoded and should be decoded, otherwise outA should be set to In, and outB should be set to 0. 
  -  In[0.5] is sent to Rom32K, which stores the Dictionary Inverse. Like before, an output of 0 means decoding has failed, and output should be the same as if signal was not encoded.
- In[12..14] stores the number of recursions. This chip only has 2 outputs, so one must only check if In[12..14] = 1 or 2.
-	If 0, Input is decoded and sent to outA only, sending 0 to outB, outC, outD.
-	If 1, Input is decoded and sent to both outA and outB.
-	If 2, Input is decoded and sent to both outA, outB, outC, and outD.

### 3.	Dictionary and Inverse: ###
-	Dictionary and Inverse are obtained by Running DictionaryCreator.py with DictionaryCreatorInput.txt as an argument. This text file teaches the Dictionary and Inverse what data to store for efficient compression. Default output files are Dictionary.hack and DictionaryInv.hack

### 4. Other Files: ###
-	There are 2 other Python Files in sources. These are DictionaryEncoder.py and DictionaryDecoder.py
-	DictionaryEncoder.py uses the same method of compression as your DictionaryEncoder.hdl to compress input data. It also shows the size difference between the input and output. Looking at this file may give clues on how to implement DictionaryEncoder.hdl.
-	DictionaryDecoder.py uses the same method of compression as your DictionaryDecoder.hdl to decompress input data. The output matches the input file of DictionaryEncoder.hdl.
-	The data in DictionaryCreatorInput.txt is the same as in DictionaryEncoder.tst, the only difference is representation in ASCII/Hex form for inputs.

## Important ##
-	Valid inputs for DictionaryEncoder must not start with a 1. This is for 2 reasons: Rom32K has only 15 address bits, and a 1 indicates an encoded signal. If input starts with a 1, encoding should automatically fail and InA should be returned.
-	Valid inputs for DictionaryDecoder must start with a 1 for the same reason as before.
#### VERY IMPORTANT: #### 
- In order to run DictionaryEncoder.tst properly, one must first load the script, and complete one step.
- Following this, View must be set to screen, and each of the 2 ROMs must be set to Dictionary.hack manually, since this cannot be done from the .tst.
<img width="689" alt="HDL" src="https://user-images.githubusercontent.com/72811430/122632881-2b4e6b80-d09b-11eb-9fa2-aa721cd1960f.png">

- Following this, the rest of the script file can be run.

## Logic Diagrams ##
### Dictionary Encoder ###

<img width="877" alt="Screen Shot 2021-06-19 at 1 12 39 AM" src="https://user-images.githubusercontent.com/72811430/122632970-98fa9780-d09b-11eb-9ff6-1063bae2982b.png">

### Dictionary Decoder ###

<img width="723" alt="Screen Shot 2021-06-19 at 1 12 55 AM" src="https://user-images.githubusercontent.com/72811430/122632979-a44dc300-d09b-11eb-9779-26e3df06e551.png">


# Dictionary Encoder and Decoder
Computers often store data using a compression algorithm to save space in memory. In this project, you will be implementing a hardware-based method of encoding and decoding data using dictionaries.

Download the description docx file to see the full explanation on the project and its implementation.


## Instructions on how to run ##
* Download the collateral provided on Canvas and use the skeletal files provided. Do not change the name of the files
* Add your full name and UIN to the introductory comment present in each .hdl file
* Implement the .hdl for each chip
* Test the basic chips using the completed .tst and .comp files provided

### Build all of the chips in the list below ###

Chip Name | File Name | Description
| :---: | :---: | :---:
DictionaryEncoder  | DictionaryEncoder.hdl | Encodes input using dictionary
DictionaryDecoder  | DictionaryDecoder.hdl | Decodes encoded input using dictionary

## How Things Work ## 
- Dictionary Encoder is a chip with 3 Inputs: Recur[3], InA[16], and InB[16]
  -  Recur stores encoded value for how many times input pattern is repeated. Value ranges from 0-7.
  - InA stores the first 16-bit pattern to be encoded.
  - InB stores the first 16-bit pattern to be encoded.

- Dictionary is loaded into both Rom32k Chips, and the address value for each is set to InA and InB respectively.
- If either rom32K returns a 0 (default), this means encoding has failed, and output will be set to InA.
- If both encodes are successful, output will be stored as
#### 1010101110101011 #### 




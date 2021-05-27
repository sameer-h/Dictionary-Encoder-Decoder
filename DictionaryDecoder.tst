load DictionaryDecoder.hdl,
output-file DictionaryDecoder.out,
compare-to DictionaryDecoder.cmp,
output-list in%B1.16.1 outA%B1.16.1 outB%B1.16.1 outC%B1.16.1 outD%B1.16.1;

// Loads Dictionary Decoder
// Program loads 2 16 bit inputs

ROM32K load DictionaryInv.hack,
output;

set in %B1010000010000010,
eval,
output;

set in %B0100001001000010,
eval,
output;

set in %B0100001101000010,
eval,
output;

set in %B0100001101000100,
eval,
output;

set in %B0100101001000100,
eval,
output;

set in %B1001010110010110,
eval,
output;
//
set in %B0100101001001111,
eval,
output;
//
set in %B0100101101001111,
eval,
output;
//
set in %B0100101101001111,
eval,
output;
//
set in %B0100101101001001,
eval,
output;
//
set in %B1001000100000100,
eval,
output;
//
set in %B0101010101001000,
eval,
output;
//
set in %B0100101001001000,
eval,
output;
//
set in %B1001010011010011,
eval,
output;
//
set in %B1001001011001011,
eval,
output;
//
set in %B1001000110000110,
eval,
output;
//
set in %B0100111001001000,
eval,
output;
//
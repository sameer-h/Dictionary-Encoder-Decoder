load DictionaryEncoder.hdl,
output-file DictionaryEncoder.out,
output-list recur%B1.3.1 inA%B1.16.1 inB%B1.16.1 out%B1.16.1 ;
compare-to DictionaryEncoder.cmp,

// Loads Dictionary Operator
// Program loads 2 16 bit inputs

//ROM32K load Dictionary.hack,
//ROM32K load Dictionary.hack,

set recur %X0002,
set inA %X4142,
set inB %X4142,
eval,
output;

set recur %X0,
set inA %X4242,
set inB %X4342,
eval,
output;

set recur %X0,
set inA %X4342,
set inB %X0,
eval,
output;

set recur %X1,
set inA %X4243,
set inB %X4243,
eval,
output;

set recur %X0,
set inA %X4344,
set inB %X4A44,
eval,
output;

set recur %X0,
set inA %X4A44,
set inB %X0,
eval,
output;

set recur %X1,
set inA %X4342,
set inB %X4342,
eval,
output;

set recur %X0,
set inA %X4A4F,
set inB %X4B4F,
eval,
output;

set recur %X0,
set inA %X4B4F,
set inB %X0,
eval,
output;

set recur %X0,
set inA %X4B4F,
set inB %X4B49,
eval,
output;

set recur %X0,
set inA %X4B49,
set inB %X0,
eval,
output;

set recur %X1,
set inA %X4A44,
set inB %X4A44,
eval,
output;

set recur %X0,
set inA %X5548,
set inB %X4A48,
eval,
output;

set recur %X1,
set inA %X5549,
set inB %X5549,
eval,
output;


set recur %X1,
set inA %X4A48,
set inB %X4A48,
eval,
output;

set recur %X1,
set inA %X4E48,
set inB %X4E48,
eval,
output;

set recur %X0,
set inA %X4E48,
set inB %X0,
eval,
output;
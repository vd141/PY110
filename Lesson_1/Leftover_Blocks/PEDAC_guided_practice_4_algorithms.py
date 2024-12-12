'''
4. algorithms

given the number of input blocks, determine how many blocks our valid structure can use

if the input is 0, our valid structure can use 0. so return the difference

if the input is 1, our valid strucutre can use 1. so return the difference

if the input is 2, our calid structure can use 1. so return the difference

if the input is 3, our valid structure can use 1. so return the difference

we determine the total number of blocks that our valid structure can use for every
layer. if there is one layer, total number of blocks used is 1. if there are two layers
the total number of blocks used is 5. if there are three layers, the total number of
blocks used is 14. every tiem we compute a layer, we compare the total sum to the input.
if the number is greater than the input, then we subtract the input from the previous total
to get the number of extra blocks.
'''
'''
Step 1: understand the problem

inputs: number of available blocks
outputs: number of blocks left over after building the tallest possible valid structure


explicit requirements: 
    - top layer is a single block
    - structure is built in layers
    - block in an upper layer must be supported by four blocks in a lower layer
    - block in lower layer can support more than one block in an upper layer
    - no spaces between blocks


implicit requirements:
    - the structure is in 3 dimensions. kind of like a square pyramid
    - the immediate lower layer has (n+1)^2 blocks as the one above it (n^2)

can a layer have blocks that don't support blocks above it? maybe these would be considered
leftover blocks

will a pyramid always have leftover blocks? not necessarily

how will we check to see if there are leftover blocks? check the total number of blocks
for a valid structure. this can be determined by summing the squares of each layer.
for example:
    - sum_of_squares = n^2 + (n+1)^2 + (n+2)^2 + (n+3)^2...
    - compare the cumulative sum at each square of n to the input. if the sum is greater, 
      subtract the difference to find the number of leftover blocks

'''
Programming: Routing Distances


CSC 311



Implementation

This project uses the sys library and a for loop to read the file to a array.

The idea behind the implementation is to first get a 2d list of the nodes with their direct costs to other nodes.
An example 2d array with the input text file should look as follows.
#0  1  2  3  4  5  <-source nodes
[ ][ ][ ][ ][ ][ ] # to reach node 0
[2][ ][ ][ ][ ][ ] # to reach node 1
[5][2][ ][ ][ ][ ] # to reach node 2
[1][2][3][ ][ ][ ] # to reach node 3
[ ][ ][1][1][ ][ ] # to reach node 4
[ ][ ][5][ ][2][ ] # to reach node 5

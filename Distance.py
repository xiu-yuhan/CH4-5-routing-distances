##Distance.py
##Elvin Lin J00711222
##Mr.Hampton
##CSC 311

import sys

#Read File to a global 2D array
def readFile(fileName):
    try:
        #opens file
        with open(fileName,'r') as file:
            #loops through entire file
            for index, line in enumerate(file,0):
                #getting amount of nodes from file
                if index == 0:
                    global amount
                    amount = int(line)
                    continue
                #getting raw line input from file
                raw.append(line)

    except FileNotFoundError:
        print(f"Error: File '{fileName}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    file.close()


def distance_vector_routing(arr):
    print(f"Distance Vector Routing:\n")
    distance = 0
    
    
#def dijkstras_algorithm(arr):
#def path_vector_routing(arr):

if __name__ == "__main__":

    ##declaring the global array that will hold the values from the input file.
    ##getting the input file if it exists
    raw = []
    #declaring variable for amount of nodes
    amount = int
    if(len(sys.argv) != 3):
        print("Usage: pyhton3 Distance.py filename.txt (source node)")
    else:
        input = sys.argv[1]
        readFile(input)

    #Setting up empty 2d array for the cost map
    #labeling the cost from source node to other node (row # and column # = node #)
    nodes = [[0 for _ in range(amount)] for _ in range(amount)]
    for i in range(len(raw)):
        nodes[int(raw[i][2])][int(raw[i][0])] = int(raw[i][4])
    for i in range(len(raw)):
        nodes[int(raw[i][0])][int(raw[i][2])] = int(raw[i][4])

    #prints the 2d array of nodes and costs for testing purposes
    for i in range(len(nodes)):
        print(str(nodes[i]))

    #distance_vector_routing(nodes)
    #dijkstras_algorithm(nodes)
    #path_vector_routing(nodes)
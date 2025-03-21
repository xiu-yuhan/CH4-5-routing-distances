##Distance.py
##Elvin Lin
##J00711222
##Mr.Hampton
##CSC 311

import sys

#Read File to a global 2D array
def readFile(fileName):
    try:
        with open(fileName,'r') as file:
            
            for index, line in enumerate(file,0):
                if index == 0:
                    continue
                print(line)

    except FileNotFoundError:
        print(f"Error: File '{fileName}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def distance_vector_routing(arr):
    print(f"Distance Vector Routing:\n")
    
#def dijkstras_algorithm(arr):
#def path_vector_routing(arr):
if __name__ == "__main__":

    ##declaring the global array that will hold the values from the input file.
    ##getting the input file if it exists
    nodes = []
    if(len(sys.argv) != 3):
        print("Usage: pyhton3 Distance.py filename.txt (source node)")
    else:
        input = sys.argv[1]
        readFile(input)

    print(nodes)
    #distance_vector_routing(nodes)
    #dijkstras_algorithm(nodes)
    #path_vector_routing(nodes)
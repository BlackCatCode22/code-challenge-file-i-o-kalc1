# Code Challenge File IO
#
# Python file name: __Code Challenge File IO.py____
#
# Date: ___09/20/23______
#
# Programmer's name: __Kevin_Alcocer___
#
# ********************************************************************************************

# This code reads the .txt file that includes the escape character "/n"
arrivingAnimals = open('arrivingAnimals.txt', 'r')
read_Animals = arrivingAnimals.readlines()
#print(read_Animals)

# This code will take the above and use .strip() to remove the escape characters "\n" while adding it to a list. Each line in the .txt file is now a list item. 
# Adding a .split("'") function turns the Animals_list into a list of lists. This should make it easier to work with and split into 
Animals_list = []               # <- I originally started by building a list and adding each element from read_Animals to this
for animal in read_Animals: 
    Animals_list.append(animal.strip())
    
# Each line should contain 6 substrings: 1.Animal 2.Season Born 3.Color 4.Weight 5.From 6. Country
# Will need to use split(',') at some point in order to make the above happen. <- Makes a list out of a string 

outputFile = open('outputFile.txt', 'w')    

# Using a for-loop enables me to write each seperate line into the outputFile.txt 
# However, each 'animal in Animals_list' is not on a seperate line.  
# Adding an escape character at the end of each animal in Animals_list fixes this issue. 
for animal in Animals_list:
    outputFile.write(animal)
    outputFile.write("\n")
outputFile.close()

# ********************************************************************************************
def get_species(my_str):
    # Split my_str using the character space. 
    words = my_str.split()
    # TODO: find the data type of words. What can you do with words?
    # This turns it into a list. You can use indices to take the fifth word to output the type of animal. 
    return words[4]

my_str = input("Enter the arriving animal: ")

# IndexError means an index is out of range. It is run when words equals to less than 5 indices since the program failed to return index [4] from words.

try:
    print(get_species(my_str))
except IndexError:
    print("Error: Your input must contain at least 5 words")
except:    
    print("Invalid Input")

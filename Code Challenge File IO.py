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
Animals_list = []
for animal in read_Animals: 
    animal_strip = animal.strip()
    Animals_list.append(animal_strip.split("'"))

# Each line should contain 6 substrings: 1.Animal 2.Season Born 3.Color 4.Weight 5.From 6. Country
# Will need to use split(',') at some point in order to make the above happen. <- Makes a list out of a string 

# Using this I can now see each line from the text file printed out on seperate lines, with each line being a list I can manipulate.  
for animal in Animals_list:
    print(animal[0])
    

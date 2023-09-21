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
print(read_Animals)


# Each line should contain 6 substrings: 1.Animal 2.Season Born 3.Color 4.Weight 5.From 6. Country
# Will need to use split(',') at some point in order to make the above happen. <- Makes a list out of a string 
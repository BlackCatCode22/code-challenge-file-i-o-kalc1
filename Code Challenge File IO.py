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

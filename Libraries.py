#Libraries
#import random

"""
Libraries contain several functions that have already been written but aren't
loaded in every python by default.

Expressions such as while, print, for etc will always be there when you open
python, but more neiche libraries such as random, we need to import.
Further infromation about each library can be found in pythons documentation
(website)
"""

#Lets assume we want to flip a coin, first we need our random library
import random
"""This gives us access to the whole random library
Typically we put all out imports at the top of our code immediately under
our name and title. This is to ensure that the scope of our libraries is the
whole code"""

#we need to specify which function from our library we need
coin = random.choice(["Heads", "Tails"])
#Choice takes a list and returns one of the values with equal probability
print(coin)



"""If we want to use a specific function from random, rather than call
the entire random library, we can use the following"""

from random import choice
#this makes choice a local funtion, so we can use the function on its own
"""Again we conventionally put them at the very top of our code"""

coin = choice(["Heads", "Tails"])
print(coin)


#Other functions
#Random integer

number = random.randint(1, 10)#1 is our minimum number and 10 is our maximum
#this is inclusive so the range is n = (1, 2, ..., 9, 10)


#shuffle, shuffles the list it is given so it's contents is randomly ordered
cards = ["1","2","3","4","5","6","7","8","9","10","Jack", "Queen", "King"]
random.shuffle(cards)
print(cards)#prints our shuffled list

for card in cards:#prints our cards one at a time
    print(card)



"""Statistics library"""
#useful for finding averages

import statistics

theMean = statistics.mean([34, 68, 54, 84, 23])
print(theMean)



"""System Library"""
import sys

print("The program is called ", sys.argv[0])
#argv allows you to form a list of words using the imput given by the user
#when running the code via the command line
"""The first value in the list is the name of the program."""

#sys.exit() can be used to close a program if there is an error
try:
    n = int(input("Please enter an integer: "))
except:
    sys.exit("Not an integer")




#Importing functions from a different file
"""THE FILE MUST BE IN THE SAME DIRECTORY/FOLDER"""
#this will load your entire file 
from Functions import hello
"""from Functions.py"""
hello()




""" CSV Library"""

#CSV reader is used when you want to split information with commas alread in it
"""
import csv

with open("file.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)"""


#Lets you read each line as a dictionary, using the first line as keys
"""
import csv

with open("file.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)"""

#to write to a file
"""
import csv

name = input("Please enter the name: ")
type1 = input("Please enter the first type: ")
type2 = input("Please enter the second type: ")

with open("pokemon.csv", 'a') as file:
    writer = csv.writer(file)
    writer.writerow([name, type1, type2])
    """

#to write to a dictionary to a file
"""
import csv

name = input("Please enter the name: ")
type1 = input("Please enter the first type: ")
type2 = input("Please enter the second type: ")

with open("pokemon.csv", 'a') as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "type1", "type2"])
    writer.writerow({"name": name, "type1": type1, "type2": type2})
    """

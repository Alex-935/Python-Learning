#While, DoWhile and Loops

"""
While loops keep repreating a set of processes while a certain condition
holds, we typically use a variable called i, as a counter
"""

#While loop to print meow 3 times
i = 3
while i != 0: #while i is not equal to 0
    print("meow")
    i = i-1 #We must reduce the value of i, or it will print meow infinitely

#if you do enter an endless loop, you can use ctrl + c to stop the program

#You can count up with the while loop instead of counting down
i = 0
while i < 3: #while i is less than 3
    print("woof")
    i = i+1
#in programming, we conventonally start counting from 0.

i = 0
while i < 3: #while i is less than 3
    print("woof")
    i += 1 #In python we can use this to increment by 1



"""
While loops are very useful for validationg user inputs and making sure
that whatever a user enters, meets your requirements
"""
#A program that takes an integer from the user and Quacks that many times
#first while loop, validates we get a value we can use
while True:
    n = int(input("Please enter a positive value for n: "))
    if n > 0:
        break #breaks out of the while loop
i = 0
while i < n:      
    print("Quack")
    i += 1


#for loops
for i in range(3):#range starts counting from 0, and will not exceed 3
    print("bark")#bark will be printed 3 times


for _ in range(2):#if we want a variable simply for counting, we an use an _ instead 
    print("pika pika")


#Using for loops to print a list
characters = ["Hu Tao", "Tartaglia", "Zhongli", "Keqing"]
for character in characters:
    print(character)
#Although I could use _ here, as I would then use the variable _,
#the code is far easier to read if i cuse a proper variable name


#If I don't know the length of a list, or its user inputted etc., I can use:
i = 0
for i in range(len(characters)):
    print(characters[i])

#You can treat a word like a list: This will print each letter in my word
word = "Chunchunmaru"
i = 0
for i in range(len(word)):
    print(word[i])

"""Lets assume we wanted to print a square graphically as a series of #.
i.e. a 3x3 square would look like:
                                    ###
                                    ###
                                    ###
We could do this with a for loop for each row and a for loop for each column
This is where we can nest for loops

It is programming convention to use i for the first for loop
and j for the second for loop. You typically wouldn't nest for loops beyond this.
"""

size = int(input("Please enter the length/width of your square: "))

for i in range(size):#For each row in our square
    for j  in range(size):#for each # in our row (the number of columns)
        print('#', end="")#prints our # upto our length
    print()#moves to a new line / creates a new row
    """Columns matter in programming, everything that has been indented once
    if part of our for i in range loop, eveything indented twice is part of
    our for j in range loop"""

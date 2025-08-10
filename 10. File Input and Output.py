#File I/O

"""When we run a program currently, all out variables are lost when the program
is closed.
But what if that information is useful?
Python allows us to store information in and read information from files.
"""

#To open a file we use the function open.
open("fileIO.txt", "w")
#if the file doesn't already exist, python will create it

"""The first parameter of our function is the file name
The second parameter is what we want to do with that file. Here are a few
second parameters we can use:
"w" - write to a file (allows us to modify its contents)"""
#Opening a file with 'w' clear your file, even if you don't write to it
"""
"r" - read a file only, we cannot change its contents, only read it
"a" - append to a file, anything written to the file will be added to what is
      already there instead of writing over it.
"""

def main():
#just opening a file doesn't do anything
#in order to wriite "Hello" to our file, we can:
    file = open("fileIO.txt", "w")
    file.write("Hello")
    file.close()


#if we want to write something else to our file, we need to use append to make
#sure we don't write over the "Hello"
    file = open("fileIO.txt", "a")
    file.write("There")
    file.close()

#main()
    
#The problem is that append is literal and we currently have "HelloThere" in our
#file. We must add the spaces ourself.


"""Another issue is it is annoying to remember to close the file each time we
are done with it. We can write our code in such a way that python open and
closes the file for us as shown below"""

def mainAppend():
    name = input("Please enter your name: ")
    with open("fileIO_2.txt", 'a') as myFile:#myFile is our variable
#equivalent to myFile = open("fileIO.txt", "a") but python closes the file after
        myFile.write(f"Hello {name}\n")
       # myFile.write(f"Hello {input('Please enter your name: ')}\n")

#mainAppend()



"""Assume I now want to read my file, there are a few ways

If i want to read it line by line, .readlines() will return each line of the
file as a list"""

def mainRead():
    with open("fileIO_2.txt", 'r') as myFile:
        lines = myFile.readlines()
    print(lines)

    for line in lines:
        print(line.rstrip())#.rstrip() removes the \n on the end of each line
        
mainRead()


def mainRead2():
    hellos = []
    with open("fileIO_2.txt", 'r') as myFile:
        for line in myFile:
            print(line.rstrip())
            for letter in line:
                print(letter)
            hellos.append(line.rstrip())#appends lines of file to list hellos
    """We can actually use a for loop to take print each line, and then each
    letter in a line

    Note we cannot sort lines taken in this way, we would need to put them
    in a list and sort them"""
    print(sorted(hellos))
    
    #or more compactly, we can sort the file instead
    with open("fileIO_2.txt", 'r') as theFile:
        for row in sorted(theFile):
            print(row.rstrip())

    
mainRead2()




"""   CSVs

CSV stands for comma seperated value. They are a very common text format used
to export data out of a variety of programs such as spreadsheets.
Each piece of data in each row is sperated by a single comma
i.e pink,blue,red,green 

CSVs are useful as we know each piece of data is seperated by exaclty one comma,
which means we can just remove those commas to get our original data back
"""

def CSV():
    row = []
    with open("PokemonCSVReordered.csv", 'r') as theFile:
        for rows in theFile:#for each row in my csv file
            row.append(rows.split(","))#split the text at each comma and form
                                        #a list (a list of each row of values)
        print(row[0])#prints the first row(our column headings)

CSV()

"""Because our pokemon csv is massive, lets limit it to gen1 so we can print
results a little more freely


Assume we want to list each pokemon and their type
We can assign each part of our row to a variable directly as follows"""
#We will use the gen1 file so we don't have over 1000 outputs
def pokeType():
    gen1Type = []
    with open("PokemonCSVGen1.csv", 'r') as theFile:
        for rows in theFile:#for each row in my csv file
            no, name, gen, type1, type2, total, hp, atk, defence, spAtk, spDef, spd, Ability1, Ability2, hAbility, height, weight,category = rows.split(",")
#above we have a variable assigned to each part of our row
#we must assign a variable to each column of our data or to none at all
#it will only store the name for the current row, and overwrite it come the next
            if type2 == "":
                gen1Type.append(f"{name} is a {type1} type.")
            else:
                gen1Type.append(f"{name} is a {type1}/{type2} type.") 
    #this is just to make sure mono-type pokemon don't have a / in their output

    for pokem in gen1Type:
        print(pokem)
    print(name)#this will only print Mew as these vairable have 1 value each
#pokeType()


"""Alternatively, a cleaner approach that would allow us to actually store this
data would be using a dictionary"""

def pokeType2():
    gen1Type = []
    with open("PokemonCSVGen1.csv", 'r') as theFile:
        for rows in theFile:#for each row in my csv file
            no, name, gen, type1, type2, total, hp, atk, defence, spAtk, spDef, spd, Ability1, Ability2, hAbility, height, weight,category = rows.split(",")
            pokemon = {"name":name, "type1":type1, "type2":type2}
            #Now each pokemon is stored as a dictionary in gen1Type so we
            #can append to the list to use their value outside of our loop
            gen1Type.append(pokemon)
            #Writting our dictionary to our list


    print(gen1Type[151])#it will print out the dictionary relating to Mew
    for pokemon in gen1Type:
        print(f"{pokemon['name']} is a {pokemon['type1']}/{pokemon['type2']} type")


pokeType2()



def pokeTypeSorted():
    gen1Type = []
    with open("PokemonCSVGen1.csv", 'r') as theFile:
        for rows in theFile:#for each row in my csv file
            no, name, gen, type1, type2, total, hp, atk, defence, spAtk, spDef, spd, Ability1, Ability2, hAbility, height, weight,category = rows.split(",")
            pokemon = {"name":name, "type1":type1, "type2":type2}
            gen1Type.append(pokemon)

    def pokeName(pokemon):#This funtion gives the name of a pokemon when called
        return pokemon["name"]

    #key is what we are ordering our output by, in this case pokemon names
    #key needs something to sort through. It cannot sort a dictionary, so we
    #refer it to the function to return the pokemon names back to it
    for pokemon in sorted(gen1Type, key = pokeName):
        print(f"{pokemon['name']} is a {pokemon['type1']}/{pokemon['type2']} type")

pokeTypeSorted()



#Alternatively we can use a lambda function
"""Lambda functions can be used when we only want use a function in one place
similar to _ in for _ in range:

it is defined quite oddly as followed
lambda parameterOfFucntion: whatIWantToReturn
"""

def pokeTypeSorted2():
    gen1Type = []
    with open("PokemonCSVGen1.csv", 'r') as theFile:
        for rows in theFile:#for each row in my csv file
            no, name, gen, type1, type2, total, hp, atk, defence, spAtk, spDef, spd, Ability1, Ability2, hAbility, height, weight,category = rows.split(",")
            pokemon = {"name":name, "type1":type1, "type2":type2}
            gen1Type.append(pokemon)

   
    #the lambda function is equivalent to def pokeName in pokeTypeSorted()
    for pokemon in sorted(gen1Type, key = lambda pokemon:pokemon["name"]):
        print(f"{pokemon['name']} is a {pokemon['type1']}/{pokemon['type2']} type")

pokeTypeSorted2()




"""Assume our data has commas within in, and is stored in a CSV file split with
commas. If we use our above approach, it will cause an issue as it is going to
split our data whenever we come across a comma, and we will end up with too
many inputs on those lines

There is a library in python called csv that has its own built in reader to deal
with these cases, where it tries to differentiate between a splitter comma and
a regular comma.

To use this, we use our reader in the same way


There are only three changes to our program, one additional line
reader = csv.reader(theFile), and changed our for loop to read from reader
instead of the file directly

finally, we deleted our .split() line as the reader is doing it for us
"""

import csv#import our csv library

def pokeTypeSorted3():
    gen1Type = []
    with open("PokemonCSVGen1.csv", 'r') as theFile:
        reader = csv.reader(theFile) #Using the function reader()
        #takes parameter of the file we are using.
        for rows in reader:#state we are setelcting rows form reader
            pokemon = {"name":rows[1], "type1":rows[2], "type2":rows[3]}
            #changed the dictionary variables as these are no longer defined
            #we could specify them in the same way in our for loop if we wanted
            #i.e. for no, name, gen, type1,...., category in reader:
            gen1Type.append(pokemon)


   
    for pokemon in sorted(gen1Type, key = lambda pokemon:pokemon["name"]):
        print(f"{pokemon['name']} is a {pokemon['type1']}/{pokemon['type2']} type")

pokeTypeSorted3()

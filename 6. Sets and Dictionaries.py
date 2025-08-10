#Sets and Dictionaries


"""Sets

A set is similar to lists and sets, but the values are unnordered and
have NO DUPLICATES

When sets are printed, the order may differ each time as the order isn't stored
If a repeat value is added to a set, it will be removed

Sets can check if a value is in that set far quicker and more efficiently than
a list or tuple. They can also very quickly compare values with other sets

sets use {}
"""

set1 = {"Maths", "History", "Physics", "CompSci", "Maths"}
print(set1)#the second "Maths has been automatically removed
print(set1)#they will give the same order for the same execution of code, but
#next time the codse is ran, it may differ


#.add('item')
"""To add something to a set, use the.add() with the thing to be added
as a parameter"""
set1.add('Music')
print(set1)


#to remove something use .remove('item')
"""Sets are unordered, you cannot remove by index"""
set1.remove('Music')
print(set1)


pokemon2 = ['Rayquaza', 'Deoxys', 'Dialga', 'Darkrai', 'Palkia', 'Arceus', 'Garchomp', 'Solgelio', 'Lunala', 'Kyogre', 'Groudon']

setPoke = set(sorted(pokemon2[7]))#this originally returned
#['R', 'a', 'a', 'a', 'q', 'u', 'y', 'z']
print(setPoke)#you will notice only one 'a' gets returned to give
#['R', 'a', 'q', 'u', 'y', 'z'] in a random order because sets don't have order


#testing if something is in a set
print("Maths" in set1)

#comparing values in sets:
set2 = {"PE", "History", "Art", "CompSci", "English"}
print(set1.intersection(set2), '\n')#returns values in both lists

print(set1.difference(set2))#returns values only in set1
print(set2.difference(set1), '\n')#returns values only in set2

print(set1.union(set2), '\n')#returns al values in both list, without duplicates

#Creating an empty set
"""If we use
emptySet = {}, this will create a dictionary, not a set

to create an empty set, we need to use;
emptySet = set()"""





#Dictionaries allow you to associate multiple values with eachother
#Dictionary consist of a key and a value and are represented as: key: value
students = {"Harry": "Gryffindor",
            "Hermione": "Gryffindor",
            "Draco": "Slytherin",
            "Severus": "Slytherin"}
#On our left we have names and on the right their houses
#The left side is our key, and we can enter that key to see the associated value
print(students["Harry"])

#If we call the variable, it will by default call the keys
for student in students:
    print(student)

#Tor print both the key and its associated value, we can use:
for student in students:
    print(student, students[student], sep = ", ")  


#Making a list of dictionaries
"""Assume we want to be able to look up a pokemon and their type 1 and type 2
seperately. We can use a list of dictionaries to assign multiple attributes
to a single entity
"""

pokedex = [
    {"name": "Charizard", "Type1": "Fire", "Type2": "Flying"},
    {"name": "Blastoise", "Type1": "Water", "Type2": None},
    {"name": "Venusaur", "Type1": "Grass", "Type2": "Poison"},
    ]

for poke in pokedex:
    print(poke["name"], poke["Type1"], poke["Type2"], sep = ", ")

#Say I wanted to print only the types of non mono-type pokemon
for poke in pokedex:
    if poke["Type2"] != None:
        print(poke["name"], poke["Type1"], poke["Type2"], sep = ", ")




#Making a pokedex that assigns a pokemon to a pokedex number
pdex = {'#001': 'Bulbasaur', '#002': 'Ivysaur', '#003': 'Venusaur'}


#.keys return our dictionary keys
print(pdex.keys())
#e.g. dict_keys(['#001', '#002', '#003'])

#.values() returns just the values
print(pdex.values())
#e.g. dict_values(['Bulbasaur', 'Ivysaur', 'Venusaur'])


#.get(key) returns the value associated with the given key
print(pdex.get('#002'))
#e.g. prints 'Ivysaur'
"""If you request a key that doesnt exist, it will return None
You can add a second arguement to specify what you want returned"""

print(pdex.get('#151'))
print(pdex.get('#151', "This pokemon hasn't been discovered"))



#.setdefault(key, valueToAssign) acts like get, but if the value doesn't exist,
#it will append it to our dictionary
print(pdex.setdefault('#001', 'Charmander'))
print(pdex.setdefault('#004', 'Charmander'))
print(pdex)



#.clear() empties your dictionary, so it will return {}
pdex.clear()
print(pdex)


pdex = {'#001': 'Bulbasaur', '#002': 'Ivysaur', '#003': 'Venusaur'}
#.pop(keyToPop) pops the given key and returns its value
venusaur = pdex.pop('#003')
print(venusaur, '\n', pdex, sep = '')

#.popitem() pops the last item of our dictionary
pdex.popitem()
print(pdex)

pdex = {'#001': 'Bulbasaur', '#002': 'Ivysaur', '#003': 'Venusaur'}

#fromkeys(iterable) takes an iterable and sets the values in it as keys in a
#dictionary
myList = ['#001', '#002', '#003']
natDex = dict.fromkeys(myList)
#variable = typeIsDictionary.fromkeys(list of keys)
print(natDex)



#.items() returns a tuple of the value pairs
print(pdex.items())

"""this is useful for iterationg over a dictionary"""
for key, value in pdex.items():
    print(key, value)



#.update() allows you to add or overwrite key-value pairs
pdex.update({'#003': 'Mewtwo', '#004': 'Mew'})
print(pdex)

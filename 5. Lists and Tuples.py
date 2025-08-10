#Lists and Tuples

"""
Lists are data types that can store as series of data
Lists are surrounded by square brackets: []
Lists start counting from zero, so we count [0th item, 1st item, 2nd item]
"""

#To print the first item in a list
pokemon = ["Deoxys", "Dialga", "Darkrai", "Palkia", "Arceus"]
print(pokemon[0])

#To print the last item in a list
print(pokemon[len(pokemon)-1])

#slice of a list. Slice is a technical term for a subset of a list
print(pokemon[1:3])
"""Will print from the second element, up to (not including)
the 3rd. It will print ["Dialga", "Darkrai"]
Our first index is inclusive, our second index is not"""

#Leaving the second number blank will give you a slice from the given number to
#the end of the list
print(pokemon[1:])# means from element 1 onwards
"""Will give ["Dialga", "Darkrai", "Palkia", "Arceus"]"""

#To count from the end of the list, we can use a negative number
print(pokemon[-2:-1])
#give ["Palkia"]
print(pokemon[-1])#print the last item in a list


"""To add values to a list"""
#Assume we want to add a pokemon to our list
#we can use .append(Variable/text) to add an item to the list

pokemon.append("Garchomp")#Adds Garchomp to my list of pokemon
print(pokemon)

"""Append always adds a value to the end of our list
If we wanted to add it to a specific spot in our list we can use insert()
Insert takes two parameters. listName.insert(position, "Value to add")
"""
#Add "Deyoxys" to the beginning of the list
pokemon.insert(0, "Rayquaza")
print(pokemon)


"""If we want to combine two lists together, we can use .extend()
extend() works for an iterable structure
listName.extend(iterableStructure)
"""
pokemon2 = ["Solgelio", "Lunala", "Kyogre", "Groudon"]
#assume we want to add the list pokemon2 onto the end of pokemon
pokemon.extend(pokemon2)
print(pokemon)

#to allow the user to add 3 pokemon to our list, we could use a for loop

for i in range(3):
    pokemon.append(input("Please enter the name of a Pokemon: ").title())
print(pokemon)
#takes in 3 pokemon names and makes the first letter a capital for consistency

#removing those 3 user-added pokemon
pokemon = pokemon[0:-3]




"""Removing items from our list
the two main ways are with .remove("itemName") or .pop()
.remove() removes the item in the list that is the same as our parameter
.pop() removes the last item in the list, and returns its value
"""
pokemon2 = pokemon#i want to leave Pokemon intact, so we will remove from list 2
pokemon2.remove("Arceus")
pokemon2.remove("Dialga")
print(pokemon2)


pokemon2 = pokemon
#because pop returns the value, we can assign it to a variable, or return it
#from a function
poppedPokemon = pokemon2.pop()
print(poppedPokemon, "has been removed from the list. \nThe list now looks like: ", pokemon2)



#After our user has added some pokemon of our own, we may want to sort the list
#so it is in alphabetical ordder. For that we can use the function sorted()
print(sorted(pokemon))
"""There is a version of sorted called sort() but this PERMANANTLY sorts the
original list while sorted doesn't change the original list"""


#Sorted() can sort anything that can be iterated, not just lists
"""If we wanted to order every letter in a pokemons name for instance we could
do the following

Bear in mund that pokemon[0] is the string Rayquaza so it is ordering the string"""
print(sorted(pokemon[0]))
"""You will notice the output was ['R', 'a', 'a', 'a', 'q', 'u', 'y', 'z']
This is because capital letters are ordered above lower case letters
to fix this we could:
"""
print(sorted(pokemon[0].lower()))#although the r is now lower case


"""Adding the key parameter to our sorted function, we can state what we want
to sort by, in this case we can sort by the lower case version of each letter
which leaves the R an upper case in our output"""
print(sorted(pokemon[0], key = str.lower))



#If instead we want to sort in a reverse order, we can add reversed = True to
#the end. It is set to false by default
print(sorted(pokemon, reverse = True))

#Alternatively we can use .reverse()
pokemon2 = pokemon
pokemon2.reverse()#this will permanently reverse the list
"""reverse() also has to be applied to a vairable, you cannont so something like
sorted(pokemon).reverse() because sorted(pokemon) is not a variable"""
print("Alternatively :", pokemon2)


"""To check if a value is in our list, we can use .index(listName)
if the value is in the list, it will return its index position in the list
if it is not, it will return a value error"""
pokemon = ["Deoxys", "Dialga", "Darkrai", "Palkia", "Arceus", "Solgelio", "Lunala", "Kyogre", "Groudon"]
print("The index of Darkrai is:", pokemon.index("Darkrai"))
#pokemon[2] == Darkrai, so it will return 2


#if we try searching for something not in the list, we get a valueerror
try:
    print("The index of Metagross is:", pokemon.index("Metagross"))
except ValueError:
    print("\nMetagross is not in the list")


"""If instead of an index, we want True if it is in the list and False if it is
not, we can use in"""
if ("Celebi" in pokemon) == False:
    print("Celebi is not in the list\n")
else:
    print("Celebi is in the list")



"""If we want the item and its index, we can use enumerate()
enumerate(iterable, start=int) returns the index first and then the item"""
for index, poke in enumerate(pokemon, start = 0):
    print(poke, "has an index of", index)



"""If we had a list of numbers"""
numbers = [5,3,5,7,7,3,2,4,6,12]
print("\nThe smallest number is:", min(numbers))
print("The largestt number is:", max(numbers))
print("The sum of the numbers in my list is:", sum(numbers), '\n')



#Converting a list to a string and back
#From a list to a string:
myList = ["Ash", "Misty", "Brock", "Dawn"]

listStr = "_".join(myList)#variable = "seperator In String".join(listName)
print("\nMy list as a string is:", listStr)

newList = listStr.split("_")#vairable = listName.split(seperator)
print("My string back as a list is:", newList, '\n')




"""Tuples

Tuples are similar to lists but unlike lists, tuples cannot be modified
In Computwer Science, we call something that cannot be modified immutable

Lists - Mutable, can be modified, use square brackets []
Tuples - Immutable, cannot be modified, use curly brackets ()


This can be useful because of how lists work."""
list1 = ["Maths", "History", "Physics", "CompSci"]
list2 = list1

list1[0] = "Geography"

print(list1, '\n', list2, '\n', sep = "")
#When we run this we can see both lists changed as they are referring to the
#same object

"""As long as we know we don't want to modify our list, we can use tuples to
ensure that the values don't need to change"""
tuple1 = ("Maths", "History", "Physics", "CompSci")
print(tuple1)



#tuple1[0] = "Geography"
"""This would give an error as once tuples are initialised, they cannot be
modifed, they are immutable"""



#to convert between lists and tuples, we can use the inbuilt function
list3 = list(tuple1)
tuple2 = tuple(list1)
print(list3, '\n', tuple2, '\n', sep="")



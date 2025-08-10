#Loops

"""
Equalities

Greater than: >
Greater than or equal to: >=
Less than: <
Less than or equal to: <=

Equals: ==
Not Equal to: !=
"""

#If Statements
"""If statements allow us to compare variables and take different actions
depending on the outcome of our comparisons"""

x = int(input("Please enter the value of x: "))
y = int(input("Please enter the value of y: "))


#If condition one is met, the first section will be ran.
if x > y:
    print("x is bigger than y")
#Elif is short for "else if". If second condition is met, this part is ran
elif x < y:
    print("x is less than y")
#Else has no condition, if the first two conditions are not met, it always runs
else:
    print("Both numbers are the same")

"""Python only checks the conditions until one is met.
It will not check the if section if the if condition is not met
It will also not check anything past the first condition that has been met.
I.e. If the "if" condition holds true, it will not check "elif" or "else" at all
"""

#Example of ticket prices
age = int(input("Please enter your age: "))
if age < 10:
    print("Children under 10 enter for free")
elif age < 18:
    print("You require a children's ticket")
elif age > 75:
    print("Pensioners can enter for free")
else:
    print("You require an adult ticket")
#This is poor practice as our Childrens ticket age range is poorly defined
#This only works beause Python only checks your if statement until the first
#condition is met and no further. So for any age under 10, it won' check your
#first elif statement at all

"""
Boolean Logic

OR: or
AND: and
NOT: !=
XOR (Exclusively Or): 

TRUE: True
FALSE: False
"""

#We are assuming only these 3 weather states exist
Sunny = True
Raining = True
Snowing = False

if Sunny == True and Raining == True:
    print("There is a rainbow")
elif Raining == True or Snowing==True:
    print("It is precipitating")
else:
    print("It is sunny outside")


#Adjusting our Examole of Ticket prices
    #Example of ticket prices
age = int(input("Please enter your age: "))
if age < 10:
    print("Children under 10 enter for free")
elif age >=10 or age < 18:
    print("You require a children's ticket")
#elif 10 <= age < 18:
elif age > 75:
    print("Pensioners can enter for free")
else:
    print("You require an adult ticket")


#match statements:
#Takes in the name of a pokemon and returns their type
pokemonName = input("Please enter a Gen 1 starter Pokemon: ").title()
if pokemonName == "Charmander":
    print(pokemonName, "is a fire type.")
elif pokemonName == "Charmeleon":
    print(pokemonName, "is a fire type.")
elif pokemonName == "Charizard":
    print(pokemonName, "is a fire/flying type.")
elif pokemonName == "Squirtle":
    print(pokemonName, "is a water type.")
elif pokemonName == "Wartortle":
    print(pokemonName, "is a water type.")
elif pokemonName == "SBlastoise":
    print(pokemonName, "is a water type.")
elif pokemonName == "VBulbasaur":
    print(pokemonName, "is a grass/poison type.")
elif pokemonName == "Ivysaur":
    print(pokemonName, "is a grass/poison type.")
elif pokemonName == "Venusaur":
    print(pokemonName, "is a grass/poison type.")
else:
    print("They are not a gen 1 starter Pokemon")

#instead of using long if statements, we can use a match statements
    #(similar to switch statement in other languages
match pokemonName:
    case "Charmander":
        print(pokemonName, "is a fire type.")
    case "Charmeleon":
        print(pokemonName, "is a fire type.")
    case "Charizard":
        print(pokemonName, "is a fire/flying type.")
    case "Squirtle":
        print(pokemonName, "is a water type.")
    case "Wartortle":
        print(pokemonName, "is a water type.")
    case "Blastoise":
        print(pokemonName, "is a water type.")
    case "Bulbasaur":
        print(pokemonName, "is a grass/poison type.")
    case "Ivysaur":
        print(pokemonName, "is a grass/poison type.")
    case "Venusaur":
        print(pokemonName, "is a grass/poison type.")
    case _:
        print("They are not a gen 1 starter Pokemon")

#Many of our pokemon have the same types, to put these in a single line:
match pokemonName:
    case "Charmander" | "Charmeleon":
        print(pokemonName, "is a fire type.")
    case "Charizard":
        print(pokemonName, "is a fire/flying type.")
    case "Squirtle" | "Wartortle" | "Blastoise":
        print(pokemonName, "is a water type.")
    case "Bulbasaur" | "Ivysaur" | "Venusaur":
        print(pokemonName, "is a grass/poison type.")
    case _:
        print("They are not a gen 1 starter Pokemon")   

#Object-Oriented Programming

def mainProcedural():
    name, type1, type2 = pokeDetails1()

    if type2 == '' or type2 == None:
        print(f"{name} is a {type1} type")
    else:
        print(f"{name} is a {type1}/{type2} type")


def pokeDetails1():
    name = input("Please enter the Pokemon's name: ")
    type1 = input("Please enter the Pokemon's first type: ")
    type2 = input("Please enter the Pokemon's second type: ")
    return name.capitalize(), type1.capitalize(), type2.capitalize()


if __name__ == "__mainProceduralX__":
    mainProcedural()



"""
Class - allow you to create your own data types and give them a name
Classes conventionally have capitals at the start of their name

Object - The instance of a class. Something that has been created using a class
Attrbutes - values an object has
Methods - functions of an object
"""

class PokemonFirst:
    ...
    
def mainOOP():
    poke1 = pokeDetails2()
    
    if poke1.type2 == '' or poke1.type2 == None:
        print(f"{poke1.name} is a {poke1.type1} type")
    else:
        print(f"{poke1.name} is a {poke1.type1}/{poke1.type2} type")


def pokeDetails2():
    poke1 = PokemonFirst()#poke1 is an object of the class Pokemon
    
    poke1.name = (input("Please enter the Pokemon's name: ")).capitalize()
    poke1.type1 = (input("Please enter the Pokemon's first type: ")).capitalize()
    poke1.type2 = (input("Please enter the Pokemon's second type: ")).capitalize()
    #name, type1 and type2 are attributes of the object poke1
    return poke1


if __name__ == "__mainOOPx__":
    mainOOP()




"""
Using our class, we can specify which values we will accept for each attribute
By passing vairables to out class via its corresponding function, we can
validate each input.

__init__ - used to initialise the contents of an object from a class
we ALWAYS need the parameter of self as the first parameter
as self allows python to assign values to the current object that has just been
created

This is because when we initialise an object, it doesnt have a name, so self
allows python to assign to the current object before its gotten a name
"""
class Pokemon2:
    def __init__(self, name, type1, type2):#short for initialse method
        self.name = name
        self.type1 = type1
        self.type2 = type2
    
def mainOop():
    poke1 = pokeDetails3()
    
    if poke1.type2 == '' or poke1.type2 == None:
        print(f"{poke1.name} is a {poke1.type1} type")
    else:
        print(f"{poke1.name} is a {poke1.type1}/{poke1.type2} type")


def pokeDetails3():
    
    name = (input("Please enter the Pokemon's name: ")).capitalize()
    type1 = (input("Please enter the Pokemon's first type: ")).capitalize()
    type2 = (input("Please enter the Pokemon's second type: ")).capitalize()
    #name, type1 and type2 are attributes of the object poke1
    
    poke1 = Pokemon2(name, type1, type2)
    """This is a constructor, as it will
    create an object of Pokemon for me using the class of Pokemon as a template
    so it has a set structure, they all look the same"""
    #Every class gets a function of the same name when it is initialsed.
    #We can pass values into that function to assign attributes for an object
    
    return poke1


if __name__ == "__mainOopX__":
    mainOop()



"""
We can use a class to return an error and/or specify specific values our
attributes can take

By default, when we print an object, python will print the memory location of
the object. Obviously this isn't very helpful, so we can use the constructor
__str__ to customise what gets printed when we print an object. i.e print(poke1)
"""


class Pokemon:
    def __init__(self, name, type1, type2=None):#short for initialse method
        if not name:
            raise ValueError("There is no name given")
        if type1 not in ['Normal', "Fire", 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy']:
            raise ValueError("Invalid Type")
        if type1 not in ['Normal', "Fire", 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy']: 
            raise ValueError("Invalid Type")
        self.name = name
        self.type1 = type1
        self.type2 = type2

    def __str__(self):
        return 'This object is of type Pokemon'
    
def mainObject():
    poke1 = pokeDetails4()
    
    if poke1.type2 == '' or poke1.type2 == None:
        print(f"{poke1.name} is a {poke1.type1} type")
    else:
        print(f"{poke1.name} is a {poke1.type1}/{poke1.type2} type")


def pokeDetails4():
    
    name = (input("Please enter the Pokemon's name: ")).capitalize()
    type1 = (input("Please enter the Pokemon's first type: ")).capitalize()
    type2 = (input("Please enter the Pokemon's second type: ")).capitalize()
    #name, type1 and type2 are attributes of the object poke1
    try:
        return Pokemon(name, type1, type2)
    except:
        ...

if __name__ == "__mainObjectX__":
    mainObject()


"""
Classes can have specific methods that its objects can use
These are functions that reside inside of a class.
"""

class Pokemon5:
    def __init__(self, name, type1, type2):#short for initialse method
        if not name:
            raise ValueError("There is no name given")
        if type1 not in ['Normal', "Fire", 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy']:
            raise ValueError("Invalid Type")
        if type2 not in ['', 'Normal', "Fire", 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy']: 
            raise ValueError("Invalid Type")
        self.name = name
        self.type1 = type1
        self.type2 = type2


    def __str__(self):
        return 'This object is of type Pokemon'

    def weakness(self):
        match self.type1:
            case 'Normal':
                return ['Fighting']
            case 'Fire':
                return ['Water', 'Ground', 'Rock']
            case 'Water':
                return ['Electric', 'Grass']
            case _:
                return "Couldn't be bothered to code"
    

    
def mainObject5():
    poke1 = pokeDetails5()
    
    if poke1.type2 == '':
        print(f"{poke1.name} is a {poke1.type1} type")
    else:
        print(f"{poke1.name} is a {poke1.type1}/{poke1.type2} type")

    print("The pokemon's weakness' are:", poke1.weakness())


def pokeDetails5():
    
    name = (input("Please enter the Pokemon's name: ")).capitalize()
    type1 = (input("Please enter the Pokemon's first type: ")).capitalize()
    type2 = (input("Please enter the Pokemon's second type of press enter if it doesn't have one: ")).capitalize()
    #name, type1 and type2 are attributes of the object poke1
    try:
        return Pokemon5(name, type1, type2)
    except ValueError or AttributeError:
        pokeDetails5()

if __name__ == "__mainObject5__":
    mainObject5()

mainObject5()

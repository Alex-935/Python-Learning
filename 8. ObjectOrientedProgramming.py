#Object-Oriented Programming

def mainProcedural():
    name, type1, type2 = pokeDetails1()

    if type2 == '' or type2 == None:
        print(name, "is a", type1, "type")
    else:
        print(name, " is a ", type1,'/',type2, " type", sep = '')
"""
    if type2 == '' or type2 == None:
        print(f"{name} is a {type1} type")
    else:
        print(f"{name} is a {type1}/{type2} type")"""
    

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
    """
    if poke1.type2 == '' or poke1.type2 == None:
        print(f"{poke1.name} is a {poke1.type1} type")
    else:
        print(f"{poke1.name} is a {poke1.type1}/{poke1.type2} type")
"""
    if poke1.type2 == '' or poke1.type2 == None:
        print(poke1.name, "is a", poke1.type1, "type")
    else:
        print(poke1.name, " is a ", poke1.type1,'/',poke1.type2, " type", sep = '')


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
    """
    if poke1.type2 == '' or poke1.type2 == None:
        print(f"{poke1.name} is a {poke1.type1} type")
    else:
        print(f"{poke1.name} is a {poke1.type1}/{poke1.type2} type")
        """
    if poke1.type2 == '' or poke1.type2 == None:
        print(poke1.name, "is a", poke1.type1, "type")
    else:
        print(poke1.name, " is a ", poke1.type1,'/',poke1.type2, " type", sep = '')


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
        print(poke1.name, "is a", poke1.type1, "type")
    else:
        print(poke1.name, " is a ", poke1.type1,'/',poke1.type2, " type", sep = '')


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
"""
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
"""
"""
    def weakness(self):
        if self.type1 == 'Normal':
            return ['Fighting']
        if self.type1 == 'Fire':
            return ['Water', 'Ground', 'Rock']
        if self.type1 == 'Water':
            return ['Electric', 'Grass']
        else:
            return "Couldn't be bothered to code"
"""
    
def mainObject5():
    poke1 = pokeDetails5()
    
    if poke1.type2 == '':
        print(poke1.name, "is a", poke1.type1, "type")
    else:
        print(poke1.name, " is a ", poke1.type1,'/',poke1.type2, " type", sep = '')

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

if __name__ == "__mainObject5x__":
    mainObject5()





"""
My alternative approach from the lesson that I personally think is better
"""

class Pokemon6:
    def __init__(self, name, type1, type2 = None):
        if not name:
            raise NameError("A name has not been given")

        while type1 not in ['Normal', "Fire", 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy']:
            #raise TypeError("You have entered an invalid Pokemon type")
            type1 = input("Enter type")

        while type2 not in [None, 'Normal', "Fire", 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy']:
            #raise TypeError("You have entered an invalid Pokemon type")
            type2 = input("Enter type")
        
        self.name = name
        self.type1 = type1
        self.type2 = type2

    def __str__(self):
        return "This object has attributes of name, type1 and type2"

    def weakness(self):
        if self.type2 == None:
            if self.type1 == 'Normal':
                return [1,1,1,1,1,1,2,1,1,1,1,1,1,0,1,1,1,1]
        else:
            if self.type1 == 'Normal':
                weakness1 =  [1,1,1,1,1,1,2,1,1,1,1,1,1,0,1,1,1,1]
            elif self.type2 == 'Normal':
                weakness2 = [1,1,1,1,1,1,2,1,1,1,1,1,1,0,1,1,1,1]
            else:
                weakness1 = list()
                weakness2 = list()#just to prevent errors
                
            for i in weakness1:
                weakness1[i] = weakness1[i] * weakness2[i]
            return weakness1


def mainx():
    poke1 = pokeDetails6()

    print(poke1)

    if poke1.type2 == None:
        print(poke1.name, "is a", poke1.type1, "type")
    else:
        print(poke1.name, " is a ", poke1.type1,'/',poke1.type2, " type", sep = '')
    #print(type(poke1))

    print("The weakness chart for ", poke1.name, " is ", poke1.weakness(), sep = '') 

def pokeDetails6():
    #poke2 = Pokemon()
    
    name = input("Please enter the Pokemon's name: ").capitalize()
    type1 = input("Please enter the Pokemon's first type: ").capitalize()
    type2 = input("Please enter the Pokemon's second type: ").capitalize()


    if type2 == '':
        poke1 = Pokemon6(name, type1)
    else:
        poke1 = Pokemon6(name, type1, type2)
    
    return poke1



"""
It is possible to change the value of attributes after they have been created
Below if I define the object poke1, the __init__ method will ensure type1
and type2 have valid values.

If I use poke1.type1 = "Sus" after they have been defined, I can change the
value while cirumventing the various checks because __init__ is only called
when the object if first created.

To get around this, we can use a property and decorators. Decorators modify
other functions.

By forcing a user to go through a function to set the value of an attribute,
we can ensure that value checks arent bypassed.
We will do this by useing getter and setter functions
"""


class Pokemon7:
    def __init__(self, name, type1, type2 = None):
        """
        if not name:
            raise NameError("A name has not been given")
        
        while type1 not in ['Normal', "Fire", 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy']:
            #raise TypeError("You have entered an invalid Pokemon type")
            type1 = input("Enter a valid type 1: ").capitalize()

        while type2 not in [None, 'Normal', "Fire", 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy']:
            #raise TypeError("You have entered an invalid Pokemon type")
            type2 = input("Enter a valid type 2: ").capitalize()
        """
        #Even in the __init__ function, the setter will be called
        #so we no longer need our error checking up here
        self.name = name
        self.type1 = type1
        self.type2 = type2

    def __str__(self):
        return "This object has attributes of name, type1 and type2"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise NameError("A name has not been given")
        self._name = name
        
    #Getter - a function for a class that gets an attribute's value
    """To indicate this is a getter, we use the decorator @property above
    our function, and name our getter exactly the same as my attribute"""
    @property
    def type1(self):
        return self._type1
    #because my instance variable and my getter/setter method are called
    #type1, I cannot have my variable in my getter and setter share the 
    #exact same name as two variables would share the same name
    """By convention, we put an underscore infront of the variable in the
    setter and getter so they aren't confused"""

    #Setter - a function that sets a value for an attribute
    """To indicate this is a setter, we use the decorator @_attribute_.setter
    above our function, and name our getter exactly the same as my attribute"""
    @type1.setter
    def type1(self, type1):
        if type1 not in ['Normal', "Fire", 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy']:
            raise ValueError("Invalid type")
        self._type1 = type1

    #Getter - a function for a class that gets an attribute's value
    """To indicate this is a getter, we use the decorator @property above
    our function, and name our getter exactly the same as my attribute"""
    @property
    def type2(self):
        return self._type2

    #Setter - a function that sets a value for an attribute
    """To indicate this is a setter, we use the decorator @_attribute_.setter
    above our function, and name our getter exactly the same as my attribute"""
    @type2.setter
    def type2(self, type2):
        if type2 not in [None, 'Normal', "Fire", 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy']:
            raise ValueError("Invalid type")
        self._type2 = type2

    def weakness(self):
        if self.type2 == None:
            if self.type1 == 'Normal':
                return [1,1,1,1,1,1,2,1,1,1,1,1,1,0,1,1,1,1]
        else:
            if self.type1 == 'Normal':
                weakness1 =  [1,1,1,1,1,1,2,1,1,1,1,1,1,0,1,1,1,1]
            elif self.type2 == 'Normal':
                weakness2 = [1,1,1,1,1,1,2,1,1,1,1,1,1,0,1,1,1,1]
            else:
                weakness1 = list()
                weakness2 = list()#just to prevent errors
                
            for i in weakness1:
                weakness1[i] = weakness1[i] * weakness2[i]
            return weakness1


def main7():
    poke1 = pokeDetails7()

    print(poke1)
    """poke1.type1 = "Sus" """
    #When python sees a call for a value change, and sees a function of the
    #exact same name as the attribute being accessed, it will automatically
    #default to the setter function

    if poke1.type2 == None:
        print(poke1.name, "is a", poke1.type1, "type")
    else:
        print(poke1.name, " is a ", poke1.type1,'/',poke1.type2, " type", sep = '')
    #print(type(poke1))

    print("The weakness chart for ", poke1.name, " is ", poke1.weakness(), sep = '') 

def pokeDetails7():
    #poke2 = Pokemon()
    
    name = input("Please enter the Pokemon's name: ").capitalize()
    type1 = input("Please enter the Pokemon's first type: ").capitalize()
    type2 = input("Please enter the Pokemon's second type: ").capitalize()


    if type2 == '':
        poke1 = Pokemon7(name, type1)
    else:
        poke1 = Pokemon7(name, type1, type2)
    
    return poke1

#main7()


"""
Instance variables are associated with objects

Sometimes you want the method to be associated with the class instead,
this uses the decorator @classmethod. Class methods dont have access to the
parameter self, but it knows which object it is dealing with.
"""

"""
Taking the sorting hat from Harry Potter
Currently we would have to create the sorting hat in this way where we are
creating the hat as an object. For each student, we would need to create a
seperate hat for each student when in reality there is only one hat"""

import random

class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
        
    def sort(self, name):
        print(name, "is in", random.choice(self.houses))

def main8():
    hat = Hat()
    hat.sort("Harry")

#main8()

"""
Class method allows us to get around having to create a seperate object to
use each method

__init__ is used to create multiple objects so we won't need it
"""

#import random

class Hat2:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    #houses is now a class specific variable, so any method within the class
    #can now call it


    #instead of using self, we use cls to state we are calling the class
    """cls is short for class, we cannot use class because its used for
    creating classes"""
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

def main9():
    Hat.sort("Harry")
    #Because it's a class method, we just call the class.method() directly
    #without needing to create an object

#main9()


"""
When code gets more and more complicated, or we collaborate with other
programmers, it would be expected any code relating to a single idea is in
a single class

In our Pokemon exapmle, the pokeDetails() function was seperate from our
pokemon class

We can use class methods to clean it up
"""
#First returning to a more simple verion of the code

class Pokemon10:
    def __init__(self, name, type1, type2 = None):
        self.name = name
        self.type1 = type1
        self.type2 = type2

    def __str__(self):
        return "This object has attributes of name, type1 and type2"



def main10():
    poke1 = pokeDetails10()
    print(poke1)


    if poke1.type2 == None:
        print(poke1.name, "is a", poke1.type1, "type")
    else:
        print(poke1.name, " is a ", poke1.type1,'/',poke1.type2, " type", sep = '')



def pokeDetails10():
    name = input("Please enter the Pokemon's name: ").capitalize()
    type1 = input("Please enter the Pokemon's first type: ").capitalize()
    type2 = input("Please enter the Pokemon's second type: ").capitalize()

    if type2 == '':
        poke1 = Pokemon10(name, type1)
    else:
        poke1 = Pokemon10(name, type1, type2)
    
    return poke1



#main10()


"""
We can make pokeDetails() a class function
"""

class Pokemon11:
    def __init__(self, name, type1, type2 = None):
        self.name = name
        self.type1 = type1
        self.type2 = type2

    def __str__(self):
        return "This object has attributes of name, type1 and type2"

    #as its a classmethod, i can call the method without creating an object
    @classmethod
    def details(cls):
        name = input("Please enter the Pokemon's name: ").capitalize()
        type1 = input("Please enter the Pokemon's first type: ").capitalize()
        type2 = input("Please enter the Pokemon's second type: ").capitalize()

        if type2 == '':
            type2 = None
            
        return cls(name, type1, type2)



def main11():
    poke1 = Pokemon11.details()


    if poke1.type2 == None:
        print(poke1.name, "is a", poke1.type1, "type")
    else:
        print(poke1.name, " is a ", poke1.type1,'/',poke1.type2, " type", sep = '')



#main11()





"""
Inheritance - When a subclass inherits the methods and attributes of a
superclass

Shown using a Harry Potter example
"""



class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    ...


class Professor:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    ...

#We notice that student and professor both have the attribute of name
# if we wanted to add value checking to them, we could end up duplicating
#a lot of code.
#Instead we can create a superclass for called wizard and have student and
#professor inherit those attributes.

class Wizard:
    def __init__(self, name, house):
        self.name = name

    ...


""" When we call the classes Student and Professor, their __init__ functions
are going to be called, which means that the attribute name would never get
defined.
To get around this, we can call the super classes __init__ function with the
parameters the superclass needs
"""

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...


def main12():
    student = Student("Harry, Gryffindor")
    professor = Professor("Snape", "Chad")
    #we can still call a the superclass seperately
    wizard = Wizard("Voldermort")#the Wizard class only had one attribute name

#main12()


"""
Using this concept, we can use the idea of operation overloading

"""
class Vault:
    def __init__(self, gold = 0, silver = 0, coins = 0):
        self.gold = gold
        self.silver = silver
        self.coins = coins

def __str__(self):
        return str(self.gold) + " Gold, " + str(self.silver) + ' Silver, ' + str(self.coins) + ' Coins'

def main13():
    client1 = Vault(100,50,25)
    client2 = Vault(13,8,12)

    gold = client1.gold + client2.gold
    silver = client1.silver + client2.silver
    coins = client1.coins + client2.coins
    total = Vault(gold, silver, coins)


"""What if we wanted to overload the + operator to add the various values
together instead of doing them individually
"""

class Vault:
    def __init__(self, gold = 0, silver = 0, coins = 0):
        self.gold = gold
        self.silver = silver
        self.coins = coins

    def __str__(self):
        return str(self.gold) + " Gold, " + str(self.silver) + ' Silver, ' + str(self.coins) + ' Coins'

    #the self refers to the left of the operator, and other to the right.
    def __add__(self, other):
        gold = self.gold + other.gold
        silver = self.silver + other.silver
        coins = self.coins + other.coins
        return Vault(gold, silver, coins)

def main14():
    client1 = Vault(100,50,25)
    client2 = Vault(13,8,12)
    
    total = client1 + client2
    print(total)

main14()

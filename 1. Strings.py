#Comments
"""
Multi-line comment
"""

#'\n' - New Line

print("Hello World")

name = input("What is your name? ")

# + strings concatonates them
print("Hello, " + name)

print("Hello,", name)

#sep and end are parameters of print, given in the Python documentation.
#We have simply reassigned their value from the defaults.
print("Hello World, ", name, sep="", end="")

print('\nHello, "Friend"')
print("Hello \"Friend\"")



#Format string,
#Putting an f infront of the string, tells python to format your sting differently.
print(f"Hello, {name}")


#Removes any spaces from the beginning and end of the value of name.
"""name = name.strip()"""
#Capitalises the first, and only first, letter of the value of name.
"""name = name.capitalize()"""
#Capitalises the first letter of every "word" in the string assigned to name.
#Python will capitalise the first letter after each space, it doesn't understand what a word is
"""name=name.title()"""
name=name.strip().title()
print(name)


#Split name into First name and surname.
#Assignes the parts of our name to the variables left to write. Seperated by space.
#First string until we hit a space becomes firstName, teaxt after first space is surname.
firstName, surname = name.split(" ")
print("First Name:", firstName, "\nSurname:", surname)

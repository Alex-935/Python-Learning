#Parameters are Place Holders
#Arguements are Actual Values
"""
def myFunction(parameter1, parameter2)

myFunction(Arguement1, Arguement2)
"""

#Creating a function
def hello():#   the empty brackets means my function has no parameters
    print("hello")# Everything indented is part of my funtion.


#Calling function hello()
hello()


#This function takes an arguement that is a name which the function then prints
"""Variables are only exist within the scope of a function.
This means I cannot use variables that have not been defined within my function
Parameters allow us to pass the variables into our function, so they are defined and can be used"""
def helloName(name):
    print("Hello,", name)

helloName("John")


#I can use a variable as an arguement, so the name the user inputs is what is returned
firstName = input("What is your first name? ")
helloName(firstName)

#Taking my arguement directly from the user input
helloName(input("What is your first name? "))



"""
Functions have to be defined before they can be called, therefore functions
must be fully written before we call them. Having lots of functions above our
main code is messy and distrupts a logical writing order.

To circumvent this, we instead can define a function called main() which acts as
our main code at the top our program, and we can simply call it at the end. As
main() will be our last line of code, all functions have been defined before
python executeds the main() function and we cen keep our main code at the top of
our program
"""

#Pretend this is a seperate python program.

#Functions continued
def main():
    fullName = input("Please enter your first name: ")
    helloFullName(fullName)

#We are defining the function we have called above
def helloFullName(entireName):
    print("Hello There,", entireName)

#By running main() after all functions have been fully defined,
#we can prevent a fun-time error of python not recognising our function as
#python has already decoded that function.
main()


#"New Program"
def main2():
    x = int(input("please enter your number to be squared: "))
    xSquared = square(x)
    print("Your number squared is:", xSquared)
    #print("Your number squared is:", square(x))


#return returns any values from our function, back to whatever called it
#so our values can be used elsewhere
def square(n):
    #return n*n
    #return n**2
    return pow(n, 2)

    
main2()




#New Program
#We are looking to determin if an inputted number is odd or even
def main3():
    x = int(input("Please enter your number: "))
    if isEven(x) == True:
        print("The number is Even")
    else:
        print("The number is Odd")

#Changing our parameters name so it doesn't get confused with the arguement
def isEven(n):
    if n % 2 == 0:# Modulo(%) gives the remainder, all even numbers when
        return True# divided by two have a remainder of 0.
    else:
        return False

main3()

#Condensed version of program above
def main3_2():
    x = int(input("Please enter your number: "))
    if isEven_2(x):#As our function returns True anyway, we don't need to check
                  #as (isEven(x)==True: returns True or False to python.
        print("The number is Even")
    else:
        print("The number is Odd")


def isEven_2(n):
    return True if n % 2 == 0 else False
#Same logic as version 1, but condensed on a single line
"""
def isEven_2(n):
    return n % 2 == 0"""
    #(n%2==0) returns a True or False value so this approach also works

main3_2()


#New program, Using Functions for input validation
def getNumber():
    while True:
        n = int(input("Please enter a positive value for n"))
        if n > 0:
            return n

getNumber()


###
"""When calling a function from another file, python will read the whole
file, including the main() at the bottom and then run it. To prevent this,
we can use the following"""

if __name__ == "__main__":
    main()

#when a function is called from its own file, it will be called with double
#underscores each side, when it is called externally, it will not have those
#To ensure an external file doesn't call main, we can use this.

"""As the other functions are only called within the main function, we
don't have to apply this to any other function"""

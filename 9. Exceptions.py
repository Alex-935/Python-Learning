#Handling Exceptions

"""
When we ask a user to enter an input, they may enter a value that would just
cause an error.
e.g.
Assume we have the line: number = int(input("Enter number: "))
And the user enters: dog
"dog" is a string that cannot be converted into an integer and therefore,
this would produce a run-time error (an error that occured while the program was
running).

To avoid this type of error we can use try and except.
"""

try: #Python will attempt this section first
    x = int(input("Please enter a number: "))
    print("x = ", x)
except ValueError: #if its runs into an error, it runs the except: funtion
    print("Your input is not a number")
#This gives python something to run, so instead of alerting you of the issue
#and crashing, it will run your except statement instead because you have
#told python you expect this error may occur.

"""
We need to specify the error we expect to deal with. These errors are the
same errors given in your error messages when running the code.

It is possible to do a "catch all", that runs if any error shows up.
The issue with this is, it may hide errors you are not expecting to come
across and make your code much harder to debug in the long run as you remain
unaware these errors even take place

A "CATCH ALL" IS BAD PROGRAMMING PRACTICE, ALWAYS SPECIFY YOUR ERROR
"""

#We want to only have things in our try function that actually could casue an
#error. The print statement is unlikely to cause an error so we want that outside
#of our try function.

try: #Python will attempt this section first
    x = int(input("Please enter a number: "))
except ValueError: #if its runs into an error, it runs the except: funtion
    print("Your input is not a number")
else:
    print("x = ", x)

"""It may help to think of your except as your if statement.
What is happening is we run our else staement if we run into no exception cases
So we will run our try statement, and if there are no issues, else will be ran.
This allows us to check the input is suitable before printing it but ensures
that everything that would cause an error is defined.
"""

#If we just had the print line underneath, that would cause a different issue
"""
e.g.
try: #Python will attempt this section first
    x = int(input("Please enter a number: "))
except ValueError: #if its runs into an error, it runs the except: funtion
    print("Your input is not an integer")

print("x = ", x)
"""
#In this instance, we would run our try statement, and if our input was not an
#integer, it would run our except line. In this scenario, no value would be
#assigned to x, and therefore x would be an undefined variable.

#This means that when we came to exectue our print line, we would get an error
#for using an undefined vairable.
#As out ellse statement only runs if our try was successful, we don't get that
#error in our above example.





#The approach above does prevent our code from crashing, but doesn't solve our
#main issue, we still don't have an integer value assigned to number
#To fix this, we can use a while loop

while True:#Will endlessly loop
    try: 
        x = int(input("Please enter a number: "))
    except ValueError:
        print("Your input is not an integer")
    else:#if our try function works, we move to else, and break out of our loop
        break

print("x = ", x)



"""the function return is stronger than break, the value will be returned
regardless of the codes state. Thusly, we can use return to break out of a loop
"""

def main():
    x = getInt()
    print("x = ", x)

def getInt():
    while True:#Will endlessly loop
        try: 
            x = int(input("Please enter a number: "))
            #return int(input("Please enter a number: "))
        except ValueError:
            print("Your input is not an integer")
        else:#if our try function works, we move to else, and break out of our loop
            return x

main()



"""
If we want to catch an error, to prevent python crashing, but we don't
want to do anything in responce to the error, we can use pass"""

def main2():
    x = getInteger()
    print("x = ", x)

def getInteger():
    while True:#Will endlessly loop
        try: 
            return int(input("Please enter an integer: "))
        except ValueError:
            pass

main2()


"""Another more compact example of the above code"""

def main3():
    x = getNumber("Please enter your number: ")
    print("x = ", x)

def getNumber(prompt):
    while True:#Will endlessly loop
        try: 
            return int(input(prompt))
        except ValueError:
            pass

main3()



"""We can raise exceptions ourselves using raise"""

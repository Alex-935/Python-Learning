from UnitTestCode import square
"""Generally it is a good idea to not include spaces into programming file
names because it may cause issue if you want to import them"""

def main():
    testSquare()
    testSquare2()

"""Unit tests are pieces of code we can use to test our functions and make
sure that they run as intended.

We need to make sure we test neiche senarios as those are the ones most likely
to return unespected outputs.

Neice scenarios include: what if we put a string into an int variable,
what if we use negative/decimal numbers, what if we add spaces into our string
"""

def testSquare():
    if square(2) != 4:# if our function doesn't return 4, it will print the message
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")
    assert square(4) == 16 #if square(4) is not 16, it will produce an
                        #AssertionError
    assert square(5) == 25



def testSquare2():
    if square(-2) != 4:# if our function doesn't return 4, it will print the message
        print("-2 squared was not 4")
    if square(-3) != 9:
        print("-3 squared was not 9")
    try:
        assert square(-4) == 16
    except AssertionError:
        print("-4 squared was not 16")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")

"""We cannot test something that is being printed by a function
we con only test values that are being returned

We cannot test print("text")
but we can test return("text")

We can always print the returned result when calling the fuuntion instead of
printing the result within the function.
i.e. print(getText()) instead of calling getText() and printing within my
function"""

if __name__ == "__main__":
    main()
    

#Integers

x = 7
y = 2
z = x + y
print(z)

"""Operations
Add: +
Subtract: -
Multiply: *
Divide: /
Modulus (Remainder): %      i.e. 5%2 = 1 because there is a remainder of 1
"""

#Adding two "numbers" the user has entered
u = input("Please enter your first number: ")
v = input("Please enter your second number: ")
w = u + v
#inputs by default are a string, so the output is a concatonation of the
#strings u and v, not addition of the numbers
print(w)


#Telling python to treat the variables as an integer
w = int(u) + int(v)
print(w)


#Just making our inputs integers directly
s = int(input("Please enter your first number: "))
t = int(input("Please enter your first number: "))
r = s + t
print(r)

#Printing the summ of two integers, without defining it into variables.
print(int(input("Please enter your first number: ")) +
      int(input("Please enter your second number: ")))

#Floats allouws us to take the user input as a float/decimal number
a = float(input("Please enter your first number: "))
b = float(input("Please enter your second number: "))
print(a, '\n', b, '\n', a+b)

#Round function in documentation: round(number[, ndigits])
"""[, ...] means the part in square brackets is optional"""
dP = 4
print("a to", dP, "decimal places is:", round(a, 4),
      "\nb to", dP, "decimal places is:", round(b, 4),
      "\nTheir sum to the nearest integer is:", round(a + b))
#round() by default rounds to the nearest whole number
print("a to 2 decimal places is:", f"{a:.2f}")


#Adding a seperator to large numbers. i.e. 1,000 instead of 1000
#The symbol following your colon, will be you seperator for every three digits
n = 123456789
print("Without the seperator, we get:", n)
print("With the seperator, we get:", f"{n:,}")




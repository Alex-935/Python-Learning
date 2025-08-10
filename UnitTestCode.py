def main():
    x = int(input("Please enter a value for x: "))
    print("x squared is: ", square(x))

def square(n):
    return n + n
    #return n**2

if __name__ == "__main__":
    main()

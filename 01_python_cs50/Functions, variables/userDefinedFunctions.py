# Defining the hello function
# this function is without any parameters and it will just print hello when called
# def hello():
    # print("Hello")

# name = input("What is your name? ")
# hello()
# print(name)

# now lets see what happens if we use parameters in the function
# def hello(to):
#     print(f"hello,", to)

# name = input("What is your name? ")
# hello(name) # this will print hello, <name> where <name> is the name

# default parameter values in functions


#now discussing scope in functions
# def main():
#     name = input("What is your name? ")
#     hello()

# def hello():
#     print("hello,", name) # this will give an error because name is defined in main() function and it is not accessible in hello() function
#     main() # this will give an error because main() function is defined after hello() function and it is not accessible in hello() function


# now lets discuss return values in functions
def main():
    x = int(input("What is x? "))
    print("x squared is", square(x)) 

def square(n):
    return n * n
main() # this will print the square of x where x is the number entered by the user
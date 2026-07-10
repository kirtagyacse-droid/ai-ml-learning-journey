#x = 1
#y = 2
#z = x + y
#print(z)

#x = input("What is x? ")
#y = input("What is y? ")
#z = x + y this will print z as 12 because x and y are treated here as strings.
#so we have to convert them into integers using int() function
#z = int(x) + int(y)
#print(z)

# now saving some lines of code by doing what we did above in a different way
x = int(input("What is x? "))
y = int(input("What is y? "))
print(x + y)
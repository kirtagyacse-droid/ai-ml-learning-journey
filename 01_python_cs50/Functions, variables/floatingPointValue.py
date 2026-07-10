x = float(input("Enter a number: "))
y = float(input("Enter another number: "))
# print(x + y) # this will print the sum of x and y

#z = round(x+y) # this will round the sum of x and y to the nearest integer
#print(z) #this will print the rounded sum of x and y
#print(f"{z:,}") #this will print the rounded sum of x and y with commas as thousands separator like if we x:1, y:999 then z = 1,000 (formatted with commas in US way)

z = round(x/y, 2) # this will round the division of x and y to 2 decimal places
print(z)
# we can also do this rounding decimal upto 2 decimal places as below:
print(f"{z:.2f}") # this will print the division of x and y upto 2 decimal places
# the above thing is called f-string approach

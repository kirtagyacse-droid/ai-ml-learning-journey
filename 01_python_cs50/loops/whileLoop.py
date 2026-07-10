# print("meow")
# print("meow")
# print("meow")

# not a good practice to repeat

# while loop

print("incrementing way")
i = 1
while i <= 3:
    print("meow")
    i += 1

print("initializing with i =0")
i = 0
while i < 3:
    print("meow")
    i += 1

print("decrementing way")
i = 3
while i != 0:
    print("meow")
    i -= 1

#one more thing continue and break
while True:
    n = int(input("Enter n: "))
    if n<0:
        print("n is negative.")
        break
    elif n > 0:
        print("n is positive")
        break
    elif n==0:
        print("n is zero")
        break
    




# print("This one is the case of ValueError")
# try:
#     x = int(input("What's x? "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not an integer")

# print("Now lets consider this better way")
# try:
#     y = int(input("What's y? "))
# except ValueError:
#     print("y is not an integer")
# else:
#     print(f"y is{y}")

# now lets consider this user should be prompted again and again untill
# the user enter the correct number
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")

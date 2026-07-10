x = int(input("What's x? "))
y = int(input("what's y? "))

# if x < y: # x < y is a boolean expression these are those expression which have straightforward answers like the this expression is either true or false 
#     print("x is less than y")

# if x > y:
#     print("x is greater than y")

# if x==y:
#     print("x is equal to y")

# elif -> after using elif it will not execute all the 3 satements as in above problem it will skip those from which the thing becomes true
# if x < y: # x < y is a boolean expression these are those expression which have straightforward answers like the this expression is either true or false 
#     print("x is less than y")

# elif x > y:
#     print("x is greater than y")

# elif x==y:
#     print("x is equal to y")

#now lets discuss else


if x < y:
    print("x is less than y")
elif x>y:
    print("x is greater than y")
else:
    print("x is equal to y")
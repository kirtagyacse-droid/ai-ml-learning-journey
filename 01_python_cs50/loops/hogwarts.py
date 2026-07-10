students = ["hermione","Harry","Ron"]

print("iterating in a list with for loop")
for i in range(3):
    print(students[i])

print("one more way")
for i in range(len(students)):
    print(students[i])

print("one more way")
for s in students:
    print(s)

print("iterating in a list with while loop")
i =0
while i<3:    
    print(students[i])
    i += 1

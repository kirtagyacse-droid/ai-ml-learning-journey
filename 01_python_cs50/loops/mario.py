print("#")
print("#")
print("#")

print("doing this the loop way")
for i in range(3):
    print("#")
print("doig the funtion way")
def main():
    print_column(3)

def print_column(height):
    for i in range(height):
        print("#")

main()

print("now printing horizzontal coins '?' of the mario")
def main():
    print_row(4)

def print_row(width):
    print('?'*width)

main()

#using the nested loops for these printing tasks
# remeber in this way outer loop will print like  3 rows 
#like:
# *
# *
# *

#now inner loop what you want to print in those 3 rows
# ***
# ***
# ***

def main():
    print_square(3)

def print_square(size):
    # for each row in square
    for i in range(size):

        #for each brick in row
        for j in range(size):

            #print brick
            print('#', end="")
        print()

main()
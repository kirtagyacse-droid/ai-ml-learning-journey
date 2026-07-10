# odd even check
# x = int(input("Enter the number: "))
# if x%2 == 0:
#     print(f"{x} is even.")
# else:
#     print(f"{x} is odd.")

# lets do this with functions
def main():
    x = int(input("Enter the number: "))
    if is_even(x):
        print("Even")
    else:
        print("odd")

# def is_even(n):
#     if n%2 == 0:
#         return True
#     else:
#         return False

# a more elegant way to write is_even function
def is_even(n):
    return (n%2 == 0)
main()
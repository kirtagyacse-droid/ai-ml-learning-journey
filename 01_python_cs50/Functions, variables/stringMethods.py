#Ask user for their name
#name = input("Enter your name? ")

#Remove whitespace from str
#name = name.strip()
#Capitalize the first letter of the first word
#name = name.capitalize()
#Capitalize the fist letter of all the words
#name = name.title()

#now no need to write that amount of code for both strip and title
#name = name.strip().title()
#and even better we can use the above thing directly where we are taking the user input
name = input("Enter your name? ").strip().title()

#Say hello to user
print(f"Hello, {name}!")
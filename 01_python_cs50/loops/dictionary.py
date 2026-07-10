students = ["Hermione","Harry","Ron","Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# we did the above thing i mean student and their houses in seperate lists
# here comes the advantage of the dictionary:

studict = {"Hermione":"Gryffindor",
            "Harry":"Gryffindor",
            "Ron":"Gryffindor",
            "Draco":"Slytherin"
            }
for student in studict:
    print(student, studict[student], sep = ",")

students = [
    {"name":"Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name":"Harry", "house":"Gryffindor", "patronus":"Stag"},
    {"name":"Ron", "house":"Gryffindor", "patronus":"Jack Russell terrier"},
    {"name":"Draco", "house":"Slytherin","patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep =",")
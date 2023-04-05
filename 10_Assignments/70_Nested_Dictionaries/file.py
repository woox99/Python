# 1. Update Vaules in Dictionaries and LIsts
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
]
sports_directory = {
    "basketball": ["Kobe", "Jordan", "James", "Curry"],
    "soccer": ["Messi", "Ronaldo", "Rooney"],
}
z = [{"x": 10, "y": 20}]

x[1][0] = 15
print(x)

students[0]["last_name"] = "Bryant"
print(students)

sports_directory["soccer"][0] = "Andres"
print(sports_directory)

z[0]["y"] = 30
print(z)

# 2. Iterate Through a list of dictionaries
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"},
]

def iterateDictionary(students):
    num = 0
    for i in range(len(students)):
        for key in students[i]:
            if num % 2 == 0:
                first = f"{key} - {students[i][key]}"
                num += 1
            else:
                last = f"{key} - {students[i][key]}"
                print(f"{first}, {last}")
                num += 1

iterateDictionary(students)

#3. Get Values From a List of Dictionaries
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"},
]

def iterateDictionary2(key_return, students):
    for i in range(len(students)):
        print(f"{students[i][key_return]}")

iterateDictionary2("first_name", students)

# 4. Iterate Through a Dictionary with List of Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_contents(dictionary):
    for key in dictionary:
        print(f"{len(dictionary[key])} {key}".upper())
        for i in range(len(dictionary[key])):
            print(dictionary[key][i])
        print("\n")

print_contents(dojo)
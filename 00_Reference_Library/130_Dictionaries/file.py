#dictionaries store "keys." Cannot have two of the same key
person = {
    "first": "Garett", 
    "Last": "Janulewicz",
    "age" : 30,
    "height" : 6
}

print(person["first"])

#changing a key in the dictionary
person["first"] = "John"

print(person["first"])

#adding a key to the dictionary
person["email"] = "garett@gmail.com"

print(person)

#testing for existing key
if "middle" not in person:
    person["middle"] = "joseph"

print(person)

#removing key
person.pop("first")
print(person)

# #BUILT IN FUCNTIONS
# len()
# type()

# #BUILT IN METHODS
# .clear() - removes all elements from dictionary
# .pop()

#LOOPING THROUGH DICTIONARY
dictionary = { "name": "Noelle", "language": "Python" }
for key in dictionary:
    print(key)
    print(dictionary[key])


# PRIMATIVE DATA TYPE
# Boolean value
is_hungry = True

# integers or float
age = 35
age2 = 3.3

# String
name = "Garett"

# COMPOSITE TYPES
# Tuples - cannot be modified after its created. can hold a group of values of mixed data types
dog = ('bruce', 'lab', 12, False )
print(dog[0])

# Lists - similar to array
empty_list = []
friends = ['tj', 'kyle', 'paige']
print(friends[1])
friends.append('jeron') #similar to .push()
print(friends)

# Dictionaries
emtpy_dictionary = {}
person = {
    'name': 'john', 
    'age': 38, 
    'weight':162
}
print(person['age'])

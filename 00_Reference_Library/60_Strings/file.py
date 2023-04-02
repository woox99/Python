name = "Garett"
print("my name is",name) #adds a space
print("my name is " + name)

#Casting nums to strings
age = 30
print("I am " + str(age) + " years old")

#Casting strings to numbers
a = 5
b = "5"
total = a + int(b)
print(total)

#f-string is similar to literal templates in js to interpolate string
first = "Garett"
last = "Janulewicz"
age = 28
print(f"My name is {first} {last}, I am {str(age)} years old")

# .format() is the old way to do f-string
print("My name is {} {}. I am {} years old".format(first, last, age))

# %-formating is the even older way to interpolate
print("My name is %s %s, I am %d years old" % (name, last, age))

# some of the many pythong string methods
# string.upper(): returns a copy of the string with all the characters in uppercase.
# string.lower(): returns a copy of the string with all the characters in lowercase.
# string.count(substring): returns number of occurrences of substring in string.

sentence = f"My name is {first} {last}, I am {age} years old"
print (sentence.upper())
num1 = 42 #variable declaration and primative numbers
num2 = 2.3 #variable declaration and primative numbers
boolean = True #variable declaration and boolean primative data type
string = 'Hello World' #variable declaration of primative string data type
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration of composite list data type
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration of composite dictionarie data type
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration of composit tuple data type
print(type(fruit)) #log statement of type check
print(pizza_toppings[1]) #log statement and access value list
pizza_toppings.append('Mushrooms') #log statment and add value dictionary
print(person['name']) #log statement and access value dictionary
person['name'] = 'George' #change value dictionary
person['eye_color'] = 'blue' #change value dicitonary
print(fruit[2]) #log statment and access value of tuple

if num1 > 45: #conditional if and access value
    print("It's greater") #log statement
else: #conditional else
    print("It's lower") #log statment

if len(string) < 5: #conditional if and length check
    print("It's a short word!") #log statement
elif len(string) > 15:  #conditional else if and length check
    print("It's a long word!") #log statement
else: #conditional else 
    print("Just right!") #log statemnt

for x in range(5): #for loop stop
    print(x) #log statment and value access
for x in range(2,5): #for loop start and stop
    print(x) #same as line 29
for x in range(2,10,3): #for loop start, stop, and increment
    print(x) #same as line 29
x = 0   #variable declaration
while(x < 5): #while loop stop
    print(x) #log statemnt and value access
    x += 1 #increment

pizza_toppings.pop() #remove from list
pizza_toppings.pop(1) #remove index 1 from list

print(person) #log statement of dictionary
person.pop('eye_color') #remove value 
print(person) #log statement of dictionary

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #condtinal
        continue #continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #conditional 
        break #break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3) #no data stored in num 3
# num3 = 72 #variable declaration
# fruit[0] = 'cranberry' #tuple cannot be changed
# print(person['favorite_team']) #no datta
# print(pizza_toppings[7]) #no data
#   print(boolean) #white space
# fruit.append('raspberry') #I think you can add to tuple
# fruit.pop(1) #connot change tuple
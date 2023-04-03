ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []

fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']

fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

salad = 3 * vegetables
print(salad)

# adding index to list
nums = [1,2,3,4,5]
nums.append(99)
print(nums)

nums_copy = nums
print(nums_copy)

# Slicing lists 
words = ["start","going","till","the","end"]
print(words[1:]) # prints ['going', 'till', 'the', 'end']
print(words[:4]) # prints ['start', 'going', 'till', 'the']
print(words[2:4]) # prints ['till', 'the']

#Built-in functions for Lists
list = [2, 6, 0]

print(len(list))

print(max(list))

# List-Methods
list = [2, 6, 0]

list.append(3)
print(list)

list.pop()
print(list)

list.reverse()
print(list)






#count down
def count_down(num):
    list = []
    for i in range(0, num+1):
        list.append(num)
        num -= 1
    return list

print(count_down(6))

#print and return
def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([3, 9]))

#first plus length
def first_plus_length(list):
    return list[0]+len(list)

print(first_plus_length([2, 6, 8]))

#values greater than second
def greater_than(list):
    new_list=[]
    num=0
    for i in range(0, len(list)):
        if list[i] > list[1]:
            new_list.append(list[i])
            num += 1
    print(str(num) + " value(s) are greater than index 2")
    return new_list

greater_than([2, 3, 4])

#This length, that value
def len_and_value(length, value):
    list = []
    for i in range(length):
        list.append(value)
    # print(list)
    return list

len_and_value(3, 7)
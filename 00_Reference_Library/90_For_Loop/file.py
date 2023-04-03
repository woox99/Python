# range(start, stop, step):

for i in range(5):
    print(f"i = {i}")

for a in range(2, 11, 2):
    print(f"a = {a}")

for x in "hello":
    print(x)

list = ["abc", 123, "xyz"]
for i in range(len(list)):
    print(list[i])

# how do we de-increment for loop?? for example if we wanted it to start at i=10 and end when i=1
for i in range(10, 0, -1):
    print(i)

# break can be used for "for-loops", when loops are next break will only exit from the inner most loop
for val in "string":
    if val == "i":
        break
    print(val)



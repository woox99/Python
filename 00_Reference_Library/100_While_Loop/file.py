i = 5
while i > 0:
    print(f"i = {i}")
    i -= 1
else: # only executes on a clean exit from the loop NOT A BREAK EXIT
    print("i is not greater than 0")

i = 0
while i < 10:
    print(f"i = {i}")
    if i == 5:
        break
    i += 1
else:
    print("else doesn't happen if the loop exits through BREAK")
#function that squares a number
def square(x):
    return x * x

print(square(5))

print(__name__)

if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)
    

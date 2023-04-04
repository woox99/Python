#define function
def say_hi(name): #parameter
    print(f"Hello, my name is {name}")

say_hi("garett") #calling funtion and argument
say_hi("alex")

# default parameter for if you want a tempary paramter in function
def greeting(name="", repeat=2):
    print(f"Hello {name}. " * repeat)

greeting("garett")
greeting(name="john", repeat=3)
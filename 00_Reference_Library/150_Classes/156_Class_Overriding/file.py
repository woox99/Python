class Parent:
    def method_a(self):
        print("invoking Parent method_a")

class Child(Parent):
    def method_a(self):
        print("involking Child method_a")

dad = Parent()
son = Child()

dad.method_a()
son.method_a()


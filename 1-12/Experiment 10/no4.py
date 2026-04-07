class Parent:
    def show(self):
        print("Inside parent show method")


class Child(Parent):
    def show(self):
        print("Inside child show method")


ch = Child()
ch.show()
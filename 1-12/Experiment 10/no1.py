class Parent:
    def parent_method(self):
        print("Properties of parent")


class Child(Parent):
    def child_method(self):
        print("Properties of child")


ch = Child()
ch.parent_method()
ch.child_method()
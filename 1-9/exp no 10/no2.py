class Grandparent:
    def gp_property(self):
        print("Inside grandparent method")


class Parent(Grandparent):
    def business(self):
        print("Inside parent business method")


class Child(Parent):
    def education(self):
        print("Inside child education method")


ch = Child()
ch.gp_property()
ch.business()
ch.education()
class Father:
    def skill1(self):
        print("Inside father's skill method")


class Mother:
    def skill2(self):
        print("Inside mother's skill method")


class Child(Father, Mother):
    def skill3(self):
        print("Inside child skill method")


ch = Child()
ch.skill1()
ch.skill2()
ch.skill3()
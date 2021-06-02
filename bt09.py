import  math
maxx = -math.inf
class Dog:
    species = 'mammal'
    def __init__(self,name,age):
        self.names = name
        self.ages = age
    def input_dog(self):
        print(f" name : {self.names} + age : {self.ages}")
def get_biggest_number(*args):
    for arg in args:
        if arg > maxx:
            maxx = arg
    return maxx
class dog:
    species = 'mammal'
    def __init__(self,name,age):
        self.names = name
        self.ages = age
    def input_dog(self):
        print(f" name : {self.names}\n"
              f" age : {self.ages}")
    def biggest(self):
        print(f"The oldest old is {get_biggest_number(self.ages)} years old")
a = dog('haha',5)
b = dog('mickey',7)
c = dog('harry',3)
a.input_dog()
b.input_dog()
c.input_dog()



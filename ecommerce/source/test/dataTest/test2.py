class User():
    def __init__(self,name,surname,old):
        self.name=name
        self.surname=surname
        self.old=old

    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name


    def __str__(self):
        return "{},  {},  {}".format(self.name,self.surname,self.old)



student1= User('ali','shams',23)
student2= User('behrang','sems',21)

student1.setName('elahe')
student1.getName()

print(student1)
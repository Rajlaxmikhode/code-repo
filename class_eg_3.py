class Person:
    def __init__(self,name):
        self.name=name
        print(f"This is {self.name}")
    def talk(self):
        print(f"{self.name} speaks English,Tamil,Hindi")
       


obj=Person("Maya")
obj1=Person("Shanaya")

#inheritance
class dog():
    def sound(self):
        print("The dog barks")
    def eat(self):
        print("Eats bones")
class cat(dog):
    def color(self):
        print("There is a white cat in my house")
    def sound(self):
        print("The cat mewos") #overrides the parent function

obj=cat()
obj.sound()
obj.eat()
obj.color()



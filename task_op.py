class Dog:
    def __init__(self,breed,age,color):
        self.breed = breed
        self.age = age
        self.color = color

    def greet(self):
        print("Hi")
        print("I am a " + self.breed + " dog.")
        print("I am " + str(self.age) + " years old")
        print("I am " + self.color + " in color")


dog = Dog('Bhuatnese',20,'black')
petdog = Dog('pug',10,'white')
myfriend_dog = Dog('German shepard',10, 'Brown')

dog.greet()
print("=============")
petdog.greet()

#Task 2
class Dog:
    def __init__(self,name,breed,age,color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

    def greet(self):
        print("Hi")
        print("My name is " + self.name )
        print("I am a " + self.breed  )
        print("I am " + str(self.age) + " years old")
        print("I am " + self.color + " in color")


dog = Dog('NAku','Bhuatnese',20,'black')
petdog = Dog('MAx','pug',10,'white')
myfriend_dog = Dog('Rob','German shepard',10, 'Brown')

dog.greet()
petdog.greet()
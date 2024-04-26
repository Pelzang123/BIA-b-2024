class Dog:
    def __init__(self,breed,age,color):
        self.breed = breed
        self.age = age
        self.color = color

    def bark (self):
        print("woof! woof!")
    
    def say_age(self):
        words_to_say = "I am " +  str(self.age) + " years old"
        print(words_to_say)

    def sleep(self):
        print("zzzzz...")

    def eat(self):
        print("nom nom nom!")

    def run(self,speed):
        print("okay, i will run in " + str(speed), 'km/hr' )
        

dog = Dog('Bhuatnese',20,'black')
petdog = Dog('pug',10,'white')
myfriend_dog = Dog('German shepard',10, 'Brown')

petdog.say_age()
dog.say_age()
myfriend_dog.say_age()
dog.run(10)

class cat:
    def __init__(self,name,species,):
        pass
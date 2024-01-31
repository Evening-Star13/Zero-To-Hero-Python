class Dog():
    
    # Class Object Attribute
    # Same for any instance of a Class
    order = 'Carnivora'
    family = 'Canidae'
    genus = 'Canis'
    species = 'Canis lupus familiaris'
    
    # Attributes
    # We take in the argument
    # Assign it using self.atribute.name
    def __init__(self, breed, name, color, age, size, temperment, spots, shots):
        self.breed = breed
        self.name = name
        self.color = color
        self.age = age
        self.size = size
        self.temperment = temperment
        
        # Boolean True/False
        self.spots = spots
        self.shots = shots
        
        # Operations/Actions ---> Methods
    def bark(self, speak):
        return(f'Woof! My name is {self.name}, {speak}!')
        
    def happy(self):
        return(f'Woof! Woof! Woof! I am so happy today I am {self.age} years old!')
    
    def fast(self):
        return("Bwahahahahaha you can't catch me I'm super speedy!!!")
    
    def cuddles(self):
        return(f"I'm very {self.temperment}!")
        
dog = Dog("German Sheppard",'Jack','Black',2,'large', 'Loving',True, True)
print(dog.breed)
print(dog.temperment)

print(dog.species)
print(dog.order)
print(dog.family)
print(dog.genus)
print(dog.bark('Woof Woof'))
print(dog.happy())
print(dog.fast())
print(dog.cuddles())



class Circle():
    
    # Class Object Attribute
    pi = 3.14
    
    def __init__(self, radius=1):
        self.radius = radius
        
    # Method
    def get_circumference(self):
        return self.radius * self.pi * 2
    

# Inheritence

class Animal():
    
    def __init__(self):
        print("ANIMAL CREATED")
        
    def who_am_i(self):
        return("I am an animal")
        
    def eat(self):
        return("I am eating")
        
class Doggy(Animal):
    
    def __init__(self, name, age):
        Animal.__init__(self)
        self.name = name
        self.age = age
        print('Dog Created')
        
    def who_am_i(self):
        return('I am a Dog!')
        
    def eat(self):
        return('I like eating') 
        
    def bark(self):
        return('Woof Woof!!')
        
pup = Doggy('Koko', 9)

print(pup.who_am_i())
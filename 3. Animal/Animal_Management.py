class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        
    def make_sound(self):
        print("Sound: ", end = '')
        if self.species == 'Dog':
            print('Woof!')
        elif self.species == 'Cat':
            print('Meow!')
        else: 
            print('Not dog and cat')

    def print_infor(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age}")
        self.make_sound()
    
animal1 = Animal("Buddy", "Dog", "1")

animal1.print_infor()


'''
class Planet:
  def __init__(self,_name):
    self.name=_name
  def printname(self):
    print(self.name)

planet1=Planet('X25')
planet2=Planet('Earth')

class Dog:
  scientific_name='Canis'
  def __init__(self,_breed,_name,_age,_weight):
    self.breed=_breed
    self.name=_name
    self.age=_age
    self.weight=_weight
  def print_dog_info(self):
    print(self.breed,self.name,self.age,self.weight,self.scientific_name)
  def bark(self):
    print('woof')

dog1=Dog('Japenese-Spitz','Punte',8,'5kgs')
dog2=Dog('German-Shephard','Bruno','4','2kgs')
dog1.print_dog_info()
dog2.print_dog_info()
dog1.bark()
'''
'''
Accessor methods - these allow us access to the data insdie the object.
These are frequently called getters as the names of these methods typically
start with the word get.

Mutator Methods - are methods that mutate or change an object in some way. Ther are frequently
called setters as they set the value of some data, and frequently start with the word set.

There is a special method in python called __str__()
[that is, __str__()] which is waht the print function prints. By default, __str__() is
class name and location in memory. We can change the this using a procedure called overriding.

'''

import math
class Planet:
    def __init__(self, _name, _radius, _mass, _distance):
        self.name = _name
        self.radius = _radius
        self.mass = _mass
        self.distance = _distance

    def get_name(self):
        return self.name
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_distance(self):
        return self.distance
    def get_volume(self):
        volume = 4/3 * math.pi * float(self.radius) ** 3
        return volume
    def get_density(self):
        density = self.mass / self.get_volume()
        return density
    def set_name(self, new_name):
        self.name = new_name
    def set_radius(self, new_radius):
        self.name = new_radius
    def set_mass(self, new_mass):
        self.mass = new_mass
    def set_distance(self, new_distance):
        self.distance = new_distance
    def __str__(self):
        msg = ""
        msg += f'hello {self.name}, how are you?'
        return msg
planet1 = Planet('X25', 4567, 56789, 56)
planet2 = Planet("z37", 1235, 67890987, 4567)

#print(planet1.get_name()), 
#print(planet2.get_volume())

print(planet1)
print(planet2)
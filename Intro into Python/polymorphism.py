class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Boat:
    def move(self):
        print("Sailing 🚤")

class Animal:
    def move(self):
        print("Walking 🐾")

# Polymorphism in action
def demonstrate_movement(entity):
    entity.move()

# Create instances
car = Car()
plane = Plane()
boat = Boat()
animal = Animal()

# Demonstrate movement
entities = [car, plane, boat, animal]
for entity in entities:
    demonstrate_movement(entity)
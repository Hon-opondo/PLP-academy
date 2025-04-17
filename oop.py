class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True  # Added attribute
        self.age = 0  # Added attribute

    def __str__(self):
        return f"{self.name} ({self.species}), Age: {self.age}, Alive: {self.is_alive}"

    def move(self):
        print(f"{self.name} moves.") # Default implementation
        raise NotImplementedError("Subclasses must implement the move() method.")

    def eat(self, food):
        print(f"{self.name} eats {food}.")

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")

    def die(self):
        self.is_alive = False
        print(f"R.I.P. {self.name}")

class Dog(Animal):
    def __init__(self, name, breed, owner=None):
        super().__init__(name, species="Dog")  # Call the Animal class constructor
        self.breed = breed
        self.owner = owner

    def __str__(self):
        owner_str = f", Owner: {self.owner}" if self.owner else ""
        return f"{super().__str__()} , Breed: {self.breed}{owner_str}" #Calls the Animal class __str__

    def move(self):
        print(f"{self.name} runs and barks.")

    def fetch(self, item):
        print(f"{self.name} fetches the {item}.")

    def bark(self):
        print(f"{self.name} says Woof Woof!")

class Cat(Animal):
    def __init__(self, name, color, lives=9):
        super().__init__(name, species="Cat")
        self.color = color
        self.lives = lives

    def __str__(self):
        return f"{super().__str__()} , Color: {self.color}, Lives: {self.lives}"

    def move(self):
        print(f"{self.name} walks stealthily.")

    def meow(self):
        print(f"{self.name} says Meow!")

    def lose_life(self):
        if self.lives > 0:
            self.lives -= 1
            print(f"{self.name} lost a life!  Lives remaining: {self.lives}")
            if self.lives == 0:
                self.die()  # Call the die method.
        else:
            print(f"{self.name} is out of lives.")

# Create instances of the classes
if __name__ == "__main__":
    animals = [
        Dog("Buddy", breed="Golden Retriever", owner="Alice"),
        Cat("Whiskers", color="Black", lives=7),
        Dog("Charlie", breed="German Shepherd", owner="Bob"),
        Cat("Luna", color="White"),
    ]


    print("\nDemonstrating Polymorphism with move():")
    for animal in animals:
        print(animal) 
        animal.move()  

    # Demonstrate other methods
    print("\nDemonstrating other methods:")
    animals[0].eat("kibble")  
    animals[1].meow()
    animals[2].bark()
    animals[3].birthday()
    animals[3].birthday()
    animals[3].lose_life()
    animals[3].lose_life()
    animals[3].lose_life()
    animals[3].lose_life()
    animals[3].lose_life()
    animals[3].lose_life()
    animals[3].lose_life()
    animals[3].lose_life()
    animals[3].lose_life()
    animals[3].lose_life() 
    print(animals[3])

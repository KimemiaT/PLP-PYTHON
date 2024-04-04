class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hi, my name is {self.name.capitalize()}. I am {self.age} years old and I am {self.gender}.")

# Create an instance of the Person class with the modified attributes
person1 = Person("Tracey", 24, "female")

# Call the introduce method to display the person's information
person1.introduce()

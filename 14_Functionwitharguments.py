# Function with positional required arguments
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# Function with keyword arguments
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

# Function with default argument
def introduce(name, age=30):
    print(f"My name is {name} and I am {age} years old.")

# Function with variable length arguments (using *args)
def calculate_sum(*numbers):
    total = sum(numbers)
    print(f"The sum of the numbers is: {total}")

# Example usage
if __name__ == "__main__":
    # Function with positional required arguments
    greet("Alice", 25)

    # Function with keyword arguments
    describe_pet(animal_type="dog", pet_name="Buddy")

    # Function with default argument
    introduce("Bob")  # Uses default value for age
    introduce("Charlie", 35)  # Overrides default value for age

    # Function with variable length arguments
    calculate_sum(1, 2, 3, 4, 5)
    calculate_sum(10, 20)
    calculate_sum(7)

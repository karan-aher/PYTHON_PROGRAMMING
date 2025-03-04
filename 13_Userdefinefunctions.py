# Function without argument
def greet():
    print("Hello, welcome to the Python program!")

# Function with argument
def square_number(number):
    return number * number

# Function returning a value
def add_numbers(a, b):
    return a + b

# Example usage
if __name__ == "__main__":
    # Function without argument
    greet()

    # Function with argument
    num = 5
    result_square = square_number(num)
    print(f"The square of {num} is {result_square}")

    # Function returning a value
    num1, num2 = 10, 20
    result_sum = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result_sum}")

from functools import reduce

# 1. Lambda function
# Lambda function to calculate the square of a number
square = lambda x: x * x

# 2. Map function
# Using map to square each element of a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))

# 3. Reduce function
# Using reduce to find the sum of all elements in a list
sum_of_numbers = reduce(lambda x, y: x + y, numbers)

# Demonstrating the outputs
if __name__ == "__main__":
    # Demonstrating the lambda function
    print(f"Square of 5 using lambda: {square(5)}")

    # Demonstrating the map function
    print(f"Squares of numbers using map: {squared_numbers}")

    # Demonstrating the reduce function
    print(f"Sum of numbers using reduce: {sum_of_numbers}")

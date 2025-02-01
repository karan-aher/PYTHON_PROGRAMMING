# 1. Demonstrating the use of 'while' loop
print("While loop demonstration:")
counter = 1
while counter <= 5:  # Loop will run as long as counter is <= 5
    print(f"Counter: {counter}")
    counter += 1  # Increment the counter to avoid infinite loop

# 2. Demonstrating the use of 'for' loop
print("\nFor loop demonstration:")
for i in range(1, 6):  # Looping through numbers from 1 to 5
    print(f"Number: {i}")

# 3. Demonstrating the use of 'nested for' loop
print("\nNested for loop demonstration:")
for i in range(1, 4):  # Outer loop from 1 to 3
    for j in range(1, 4):  # Inner loop from 1 to 3
        print(f"i: {i}, j: {j}")
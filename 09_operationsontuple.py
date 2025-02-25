# 1. Create a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original Tuple:", my_tuple)

# 2. Access elements in the tuple
print("Accessing first element:", my_tuple[0])  # Accessing the first element
print("Accessing last element:", my_tuple[-1])  # Accessing the last element

# 3. Print the tuple
print("Tuple contents:", my_tuple)

# 4. Delete a tuple (Tuples are immutable, but we can delete the reference to the tuple)
del my_tuple
try:
    print("After deleting tuple:", my_tuple)  # This will raise an error as tuple is deleted
except NameError as e:
    print(f"Error: {e}")

# 5. Convert tuple into list
my_tuple = (1, 2, 3, 4, 5)  # Re-creating the tuple for demonstration
my_list = list(my_tuple)
print("Tuple converted to list:", my_list)

# 6. Convert list back to tuple
new_tuple = tuple(my_list)
print("List converted back to tuple:", new_tuple)

# Demonstrating various list operations in Python

# 1. Create a List
print("Creating a list:")
my_list = [10, 20, 30, 40, 50]
print("List created:", my_list)

# 2. Access elements in the list
print("\nAccessing elements in the list:")
# Accessing elements by index
first_element = my_list[0]  # First element
last_element = my_list[-1]  # Last element
print("First element:", first_element)
print("Last element:", last_element)

# Accessing a range of elements (slicing)
sub_list = my_list[1:4]  # Elements from index 1 to 3 (excluding index 4)
print("Sub-list (from index 1 to 3):", sub_list)

# 3. Update elements in the list
print("\nUpdating elements in the list:")
my_list[2] = 100  # Changing the value at index 2 (third element) to 100
print("List after update:", my_list)

# Updating a range of elements (slicing)
my_list[1:3] = [200, 300]  # Replacing elements at index 1 and 2 with 200 and 300
print("List after range update:", my_list)

# 4. Delete elements from the list
print("\nDeleting elements from the list:")
# Deleting an element by index
del my_list[0]  # Removing the first element
print("List after deleting the first element:", my_list)

# Deleting an element by value (using remove)
my_list.remove(300)  # Removing the first occurrence of 300
print("List after removing 300:", my_list)

# Deleting the last element (using pop)
popped_element = my_list.pop()  # Removes and returns the last element
print("Popped element:", popped_element)
print("List after popping the last element:", my_list)

# Clear the entire list
my_list.clear()  # Removes all elements from the list
print("List after clearing all elements:", my_list)
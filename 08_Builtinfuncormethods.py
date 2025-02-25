# Sample list for demonstration
my_list = [10, 20, 30, 40, 50]

# 1. Using the `len()` function to get the length of the list
print("Length of the list:", len(my_list))

# 2. Using the `max()` function to get the maximum value in the list
print("Maximum value in the list:", max(my_list))

# 3. Using the `min()` function to get the minimum value in the list
print("Minimum value in the list:", min(my_list))

# 4. Using the `sum()` function to get the sum of all elements in the list
print("Sum of elements in the list:", sum(my_list))

# 5. Using the `sorted()` function to get a sorted version of the list (doesn't modify original)
sorted_list = sorted(my_list)
print("Sorted list:", sorted_list)
print("Original list after sorted (unchanged):", my_list)

# 6. Using the `reverse()` method to reverse the list in place
my_list.reverse()
print("\nList after reverse() method:", my_list)

# 7. Using the `append()` method to add an element to the end of the list
my_list.append(60)
print("\nList after append(60):", my_list)

# 8. Using the `insert()` method to insert an element at a specific index
my_list.insert(2, 25)  # Insert 25 at index 2
print("\nList after insert(2, 25):", my_list)

# 9. Using the `remove()` method to remove the first occurrence of a value
my_list.remove(40)  # Removes the first occurrence of 40
print("\nList after remove(40):", my_list)

# 10. Using the `pop()` method to remove and return the element at a specific index
popped_value = my_list.pop(1)  # Removes and returns the element at index 1
print("\nPopped value from index 1:", popped_value)
print("List after pop(1):", my_list)

# 11. Using the `index()` method to find the index of a value
index_of_25 = my_list.index(25)  # Finds the index of 25
print("\nIndex of 25 in the list:", index_of_25)

# 12. Using the `count()` method to count how many times an element appears in the list
count_of_20 = my_list.count(20)  # Counts occurrences of 20
print("\nCount of 20 in the list:", count_of_20)

# 13. Using the `extend()` method to add multiple elements to the end of the list
my_list.extend([70, 80, 90])
print("\nList after extend([70, 80, 90]):", my_list)

# 14. Using the `clear()` method to remove all elements from the list
my_list.clear()
print("\nList after clear():", my_list)

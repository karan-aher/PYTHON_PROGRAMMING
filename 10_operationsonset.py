# 1. Create a set
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

# 2. Access elements in the set (Sets are unordered, so we can't access by index)
# But we can loop through the set to access elements
print("Accessing elements in the set:")
for item in my_set:
    print(item)

# 3. Update set (Adding new elements or updating existing ones)
my_set.add(6)  # Adding an element
print("Set after adding 6:", my_set)

my_set.update([7, 8])  # Adding multiple elements
print("Set after adding 7 and 8:", my_set)

# 4. Delete set (We can either remove an element or delete the entire set)
my_set.remove(8)  # Removes element 8
print("Set after removing 8:", my_set)

# To delete the set itself:
del my_set
try:
    print("After deleting the set:", my_set)  # This will raise an error since the set is deleted
except NameError as e:
    print(f"Error: {e}")



# Function to create a dictionary
def create_dict():
    my_dict = {
        'name': 'Alice',
        'age': 25,
        'city': 'New York'
    }
    return my_dict

# Function to access elements in a dictionary
def access_dict(my_dict, key):
    return my_dict.get(key, "Key not found")

# Function to update elements in a dictionary
def update_dict(my_dict, key, value):
    my_dict[key] = value
    return my_dict

# Function to delete an element from a dictionary
def delete_from_dict(my_dict, key):
    if key in my_dict:
        del my_dict[key]
        return my_dict
    else:
        return "Key not found"

# Function to loop through the dictionary
def loop_through_dict(my_dict):
    print("Looping through the dictionary:")
    for key, value in my_dict.items():
        print(f"{key}: {value}")

# Function to create a dictionary from a list of tuples
def create_dict_from_list(lst):
    return dict(lst)

# Example usage
if __name__ == "__main__":
    # Create a dictionary
    my_dict = create_dict()
    print(f"Created dictionary: {my_dict}")
    
    # Access an element in the dictionary
    print(f"Access 'name' from dictionary: {access_dict(my_dict, 'name')}")
    
    # Update an element in the dictionary
    print(f"Update 'age' in dictionary: {update_dict(my_dict, 'age', 26)}")
    
    # Delete an element from the dictionary
    print(f"Delete 'city' from dictionary: {delete_from_dict(my_dict, 'city')}")
    
    # Loop through the dictionary
    loop_through_dict(my_dict)
    
    # Create a dictionary from a list of tuples
    list_of_tuples = [('brand', 'Toyota'), ('model', 'Corolla'), ('year', 2020)]
    new_dict = create_dict_from_list(list_of_tuples)
    print(f"Created dictionary from list of tuples: {new_dict}")

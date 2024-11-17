import copy

def demonstrate_copy():
    # Original list
    original_list = [['Shallow', 2, 3], [4, 5, 6]]
    
    # Creating a shallow copy
    shallow_copy = copy.copy(original_list)
    
    # Creating a deep copy
    deep_copy = copy.deepcopy(original_list)
    
    # Modifying the original list and deep copy to show the difference
    original_list[0][0] = 'Modified'
    deep_copy[1][0] = 'Deep'
    
    # Printing results
    print("Original List:", original_list)
    print("Shallow Copy:", shallow_copy)
    print("Deep Copy:", deep_copy)

# Call the function to demonstrate
demonstrate_copy()
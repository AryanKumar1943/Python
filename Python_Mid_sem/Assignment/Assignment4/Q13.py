def sort_by_second_element(tuples_list):
    
    return sorted(tuples_list, key=lambda x: x[1])

# Example usage
tuples = [(3, 4), (1, 2), (5, 1), (4, 3)]
sorted_tuples = sort_by_second_element(tuples)
print(sorted_tuples)  
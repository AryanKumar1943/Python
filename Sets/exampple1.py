# Creating sets
fruits = {"apple", "banana", "cherry"}
citrus = {"orange", "lemon", "banana"}

# Adding elements
fruits.add("mango")

# Removing an element
fruits.discard("banana")

# Union of sets
all_fruits = fruits.union(citrus)

# Intersection of sets
common_fruits = fruits.intersection(citrus)

print("All Fruits:", all_fruits)
print("Common Fruits:", common_fruits)
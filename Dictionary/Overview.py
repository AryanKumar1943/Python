# my_dict={1:"alice","age":30,1:"1"}
# print(my_dict)
# Using curly braces
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(my_dict)
# Using dict() constructor
another_dict = dict(name="Bob", age=25, city="Los Angeles")
print(another_dict)
# Adding a new key-value pair
my_dict["job"] = "Engineer"

# Updating an existing value
my_dict["age"] = 31

# Deleting a key-value pair
del my_dict["city"]
print(my_dict)
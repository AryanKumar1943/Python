nested_dict = {
    "person": {
        "name": "Alice",
        "age": 30,
        "address": {
            "city": "New York",
            "zipcode": "10001"
        }
    }
}

print(nested_dict["person"]["address"]["city"])  # Output: New York
def outer_function():
    x = 5  # Variable in the enclosing (outer) scope

    def inner_function():
        nonlocal x  # Refers to 'x' in the outer_function scope
        x = 10      # Modifies 'x' in the outer_function
        print("Inner:", x)

    inner_function()
    print("Outer:", x)

outer_function()
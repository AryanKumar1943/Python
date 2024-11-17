def make_single(num):
    l = []  # Reset the list for each call
    for i in str(num):
        l.append(int(i))
    return sum(l)

result = make_single(1558)

while result >= 10:  # Repeat the process until the result is a single-digit number
    result = make_single(result)

print(result)

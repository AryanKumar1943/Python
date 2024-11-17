s1 = "tom marvolo riddle"
s2 = "i am lord voldemort"

# Create dictionaries to count character frequencies
my_dict1 = {}
my_dict2 = {}

# Count character frequencies for s1
for i in s1:
    if i != " ":  # Ignore spaces
        my_dict1[i] = my_dict1.get(i, 0) + 1

# Count character frequencies for s2
for j in s2:
    if j != " ":  # Ignore spaces
        my_dict2[j] = my_dict2.get(j, 0) + 1

# Check if the two dictionaries are equal
if my_dict1 == my_dict2:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

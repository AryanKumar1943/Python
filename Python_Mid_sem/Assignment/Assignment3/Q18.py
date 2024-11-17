# s = "Aman"
# vowel = "AEIOUaeiou"
# l = []

# for i in s:
#     flag = 0 
#     for j in vowel:
#         if i == j:
#             flag = 1
#             break 
#     if flag != 1: 
#         l.append(i)

# res = "".join(l)  
# print(res) 
s = "Aman"
vowel = "AEIOUaeiou"

# Using list comprehension to filter out vowels
l = [i for i in s if i not in vowel]

res = "".join(l)
print(res)  # Output: mn
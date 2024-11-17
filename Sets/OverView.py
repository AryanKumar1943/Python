my_seta={1,2,3,4}
print(my_seta)
my_setb=set([1,2,4])
print(my_setb)
my_seta.add(5)
print(my_seta)
my_seta.update([6,7])
print(my_seta)
my_seta.remove(2) #Remove an Element: Use remove() to remove an element; it raises an error if the element is not found
# Discard an Element: Use discard(), which does not raise an error if the element is absent.
my_seta.discard(3)
my_seta.clear()
#Clear the Set: Use clear() to remove all elements from the set.
set_a = {1, 2}
set_b = {2, 3}
union_set = set_a.union(set_b) # or set_a | set_b
intersection_set = set_a.intersection(set_b) # or set_a & set_b
difference_set = set_a.difference(set_b) # or set_a - set_b
sym_diff_set = set_a.symmetric_difference(set_b)
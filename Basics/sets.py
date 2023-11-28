"""
Set is an unordered collection of unique elements, used for storing and performing set operations on data.
"""
set_values = {1, 2, 3, 5, 4, 5}
print(set_values)  # Doesn't return duplicate values: {1, 2, 3, 4, 5}

print("\nadd:")
set_values.add(10)
set_values.add(2)  # set already contains 2 so it won't be added.
print(set_values)  # {1, 2, 3, 4, 5, 10}

# Set doesn't support indexing.
print(2 in set_values)
print(len(set_values))   # 6

set_values.clear()
print(set_values)  # set()

my_set = {1, 3, 5, 7, 9}
your_set = {2, 4, 7, 9}

print("\ndifference:")
print(my_set.difference(your_set))  # {1, 3, 5}

print("\ndiscard:")
my_set.discard(1)
print(my_set)  # {3, 5, 7, 9}

print("\nintersection:")
print(my_set.intersection(your_set))  # {9, 7}
'or'
print(my_set & your_set)

print("\ndisjoin:")
print(my_set.isdisjoint(your_set))  # False - Returns true if both sets doesn't have anything in common.

print("\nissubset:")
print(my_set.issubset(your_set))  # False - Returns true if your_set contains all elements present in my_set.

print("\nisSuperset:")
print(my_set.issuperset(your_set))  # False -  Returns true when my_set contains all elements present in your_set.

print("\nunion:")
print(my_set.union(your_set))  # combines both sets & removes duplicates
'or'
print(my_set | your_set)

print("\ndifference_update:")
my_set.difference_update(your_set)
print(my_set)  # Updated to {3, 5}






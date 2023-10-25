"""
A tuple is an ordered and immutable collection of elements.
Tuple is faster than list. Similar to list but immutable.
"""
my_tuple = (1, 2, 3, 5, 4, 5)
print(my_tuple[1])  # 2
print(5 in my_tuple)  # True

new_tuple = my_tuple[1:3]
print(new_tuple)  # (2, 3)

print(my_tuple.count(5))  # 2
print(my_tuple.index(5))  # 3
print(len(my_tuple))  # 6

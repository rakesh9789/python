"""
Dictionary is an unordered key value pair.
Dictionary key needs to be immutable. Key is usually something descriptive.
Key has to be unique.
"""
dictionary = {
    'a': [1,2],
    2: True,
    'x': 'Bow'
}

print(dictionary[2])  # Prints value of this key or error if not present in dictionary
print(dictionary['a'][1])  # Returns 2

print("\nget:")
print(dictionary.get('c'))  # Returns None instead of error
print(dictionary.get('c', 55))  # Returns 55 if c doesn't exist in dictionary.
print(dictionary.get('x', 20))  # Return Bow

print('x' in dictionary.keys())  # True
print("\nPrint Items:")
print(dictionary.items())

print("\nupdate:")
dictionary.update({2: 5})
print(f'Dictionary after update: {dictionary}')
# If it doesn't exist, Updates as new key
dictionary.update({'z': 'Laptop'})
print(f'Updated dictionary when key doesn\'t exist: {dictionary}')

print("\npop:")
print(dictionary.popitem())  # Removes some pair
print(dictionary.pop(2))  # Removes value of whatever got removed i.e., True

print("\nclear:")
dictionary.clear()
print(dictionary)  # {}

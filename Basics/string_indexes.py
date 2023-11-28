"""
String indexes are used to access individual characters within a string.
The indexing starts at 0 for the first character and goes up to n-1, where n is the length of the string.
You can also use negative indexing, where -1 refers to the last character, -2 to the second-to-last character, and so on.
"""
# [start:stop:step]
sentence = '0123456789'
print(sentence[1])  # 1st index character = 1
print(sentence[3:6])  # Characters from 3rd index to 5th index(n-1)=345
print(sentence[3:9:2])  # steps over by 2 = 357
print(sentence[1:])  # Stop not specified so by default goes till end = 123456789
print(sentence[:5])  # Start not specified so starts by default at 0th index = 01234
print(sentence[::2])  # 02468
print(sentence[-1])  # Negative Indexing -1=last index character i.e., 9
print(sentence[::-1])  # Reverses a string
print(sentence[::-2])  # Prints in reverse order(From last index) skips by 2 = 97531

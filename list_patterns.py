"""
You can create list patterns or sequences using various techniques and built-in functions
to generate lists with specific elements and patterns.
ex: range(), repetition operator(*), split, join, random... etc
"""

print(list(range(1, 11)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sentence = '!'
new_sentence = sentence. join(['Hi', 'Nice to meet you', '.'])
print(new_sentence)  # Hi!Nice to meet you!.


# List Unpacking
a, b, *c, d = ['Sun', 'Moon', 'Earth', 'Mars', 'Saturn']
print(f"List Unpacking - \n a is : {a} \n b is : {b} \n c is : {c} \n d is: {d}")


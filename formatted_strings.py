"""
Formatted strings, often referred to as f-strings, allow you to embed expressions and variables within
string literals. They are created by prefixing a string with the letter 'f' or 'F'. Inside these strings,
you can include variables and expressions enclosed in curly braces {} along with an optional format specifier.
"""

name = 'Mandy'
age = 23
# Usual printing
print('Hi' + ' ' + name + '.' + 'You are ' + str(age) + 'years old.')
# Formatted strings
print(f'Hi {name}.You are {age} years old')

# Python 2/3
print('Hi {1}.You are {0} years old'.format(age, name))
'or'
print('Hi {new_name}.You are {age} years old'.format(age = 20, new_name = 'Amber'))

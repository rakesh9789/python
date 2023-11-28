"""
Data Structure: A way of organizing and storing data in a structured and efficient manner.
Lists are one of the most commonly used data structures in Python, and they are versatile and flexible.
Lists are defined by enclosing a comma-separated sequence of items within square brackets [ ]
"""
# List slicing
cart = [
    'notebooks',
    'pens',
    'charger',
    'phone',
    'table'
]
print(cart[1])  # pens
print(cart[1:3])  # ['pens', 'charger']
print(cart[0::2])  # ['notebooks', 'charger', 'table']

cart[1] = 'eraser'
print(cart)  # Lists are mutable.['notebooks', 'eraser', 'charger', 'phone', 'table']

# Here both new_cart & cart are same. If we want to just copy then new_cart = cart[:]
new_cart = cart[0:]
new_cart[0] = 'laptop'
print(new_cart)
# If new_cart = cart     : ['laptop', 'eraser', 'charger', 'phone', 'table']
# If new_cart = cart[0:] :['notebooks', 'eraser', 'charger', 'phone', 'table']
print(cart)


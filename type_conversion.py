"""
Type conversion in Python, often referred to as "type casting" or "type coercion,"
is the process of converting a value from one data type to another.
1. Implicit Type Conversion (Coercion)
 - Python automatically performs certain type conversions when necessary.
2. Explicit Type Conversion (Type Casting)
 - It allows you to explicitly convert a value from one data type to another using built-in functions.
3. Custom Type Conversion:
 - You can define your own custom type conversion functions by creating functions that transform values from one data type to another.
"""
import datetime

# Get the current year
current_year = datetime.date.today().year
birth_year = input("-Q- What year were you born? ")
age = current_year - int(birth_year)  # Type conversion from str to int
print(f"Current Year is {current_year}. So, Your Age is {age} !")

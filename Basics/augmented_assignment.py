"""
Augmented assignment operators in Python are shorthand operators that combine an operation and assignment
in a single step, like +=, -=, *=, etc
Ex: a += 1 is same as a = a + 1
"""
# Example 1
value = 5
value -= 2  # In order for this to work, this variable should have some previous value.
print(value)

# Example 2
message = "Hello, "
name = "Pie!"
message += name  # Equivalent to message = message + name
print(message)

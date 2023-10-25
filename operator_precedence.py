"""
When the python interpreter encounters any expression containing several operations,
all operations get evaluated according to an ordered hierarchy called Operator Precedence.
PEMDAS(Parantheses, Exponentiation, Multiplication, Division, Addition)
All operators except exponential follows left to right associativity in case of tie.
"""

# 20 - 8 = 12
print(20 - 2 * 4)

# 17 + 8 = 25
print((20 - 3) + 2 ** 3)

# 5 + 3 * 4 // 4 = 5 + 3 * 1 = 8
print(5 + 3 * 2 ** 2 // 4)

# 10 + 12 * 3 % 34 / 8 = 10 + 36 % 34 / 8 = 10 + 2/8 = 10.25
print(10 + 12 * 3 % 34 / 8)

# Precedence of (//)>> Precedence of (+) >> Precedence of (<<) >> Precedence of(XOR)
# 4 ^ 2 << 3 + 2 = 4 ^ 2 << 5 = 4 ^ 64 = 68
print(4 ^ 2 << 3 + 48 // 24)

# right to left precedence (Exponentiation)
print(3 ** 2 ** 4)

# left to right precedence
print(4 << 8 >> 2)

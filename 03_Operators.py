# Arithmetic Operators
a = 10
b = 5
sum_ab = a + b
diff_ab = a - b
prod_ab = a * b
div_ab = a / b
mod_ab = a % b
exp_ab = a ** b
floor_div_ab = a // b

# Relational Operators
is_equal = a == b
is_not_equal = a != b
is_greater_than = a > b
is_less_than = a < b
is_greater_or_equal = a >= b
is_less_or_equal = a <= b

# Logical Operators
logical_and = (a > b) and (b > 0)
logical_or = (a < b) or (b > 0)
logical_not = not(a == b)

# Assignment Operators
c = 20
c += 5  # c = c + 5
c -= 2  # c = c - 2
c *= 3  # c = c * 3
c /= 2  # c = c / 2
c %= 3  # c = c % 3

# Bitwise Operators
x = 5  # In binary: 0101
y = 3  # In binary: 0011
bitwise_and = x & y      # Binary: 0001
bitwise_or = x | y       # Binary: 0111
bitwise_xor = x ^ y      # Binary: 0110
bitwise_not = ~x         # Binary: -0110 (two's complement)
bitwise_left_shift = x << 1  # Left shift: 1010 (in decimal, 10)
bitwise_right_shift = x >> 1  # Right shift: 0010 (in decimal, 2)

# Membership Operators
my_list = [1, 2, 3, 4, 5]
is_member = 3 in my_list
is_not_member = 10 not in my_list

# Identity Operators
is_same_object = a is b
is_not_same_object = a is not b

# Output the results
print("Arithmetic Operations:")
print(f"Sum: {sum_ab}, Difference: {diff_ab}, Product: {prod_ab}, Division: {div_ab}")
print(f"Modulo: {mod_ab}, Exponent: {exp_ab}, Floor Division: {floor_div_ab}")

print("\nRelational Operations:")
print(f"a == b: {is_equal}, a != b: {is_not_equal}")
print(f"a > b: {is_greater_than}, a < b: {is_less_than}")
print(f"a >= b: {is_greater_or_equal}, a <= b: {is_less_or_equal}")

print("\nLogical Operations:")
print(f"(a > b) and (b > 0): {logical_and}")
print(f"(a < b) or (b > 0): {logical_or}")
print(f"not (a == b): {logical_not}")

print("\nAssignment Operations:")
print(f"Updated value of c: {c}")

print("\nBitwise Operations:")
print(f"x & y: {bitwise_and}, x | y: {bitwise_or}")
print(f"x ^ y: {bitwise_xor}, ~x: {bitwise_not}")
print(f"x << 1: {bitwise_left_shift}, x >> 1: {bitwise_right_shift}")

print("\nMembership Operations:")
print(f"Is 3 in my_list? {is_member}")
print(f"Is 10 not in my_list? {is_not_member}")

print("\nIdentity Operations:")
print(f"a is b: {is_same_object}")
print(f"a is not b: {is_not_same_object}")
 

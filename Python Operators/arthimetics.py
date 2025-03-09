
# #1. Arthmetics operators

# # Additional
x = 5
y = 3
print(x + y)

# # Multiplication 
x = 3
y = 6
print(x * y)

# # subtraction
x = 2
y = 8
print(x - y)

# # Division
x = 4
y = 7
print(x / y)

# # floor division
x = 5
y = 2
print(x % y)

# # Exponentiation
x = 2
y = 3
print(x ** y)

# # modulus
x = 5
y = 2
print(x % y)

# operators with prompt
# Add operator

var1 = input("enter a first number :")
var2 = input("enter a second number:")
print(int(var1)+int(var2))

# Subtract operator

var1 = input("enter a first number :")
var2 = input("enter a second number:")
print(int(var1)-int(var2))

# Multiply operator

var1 = input("enter a first number :")
var2 = input("enter a second number:")
print(int(var1)*int(var2))

# Division operator

var1 = input("enter a first number :")
var2 = input("enter a second number:")
print(int(var1)/int(var2))

# Type conversion

var1 = 5
var2 = 3.7
var3 = "5"
print(type(var1))
print(type(var2))
print(type(var3))

# ==================================================================
# 2. Assignment Operators

x = 5
print(x)
x += 3   # x = 5 => x = 5 + 3 Ans 8
print(x)
x -= 2   # x = 8 => x = 8 - 2 Ans 6
print(x)
x *= 2   # x = 6 => x = 6 * 2 Ans 12
print(x)
x /= 3   # x = 12 => x = 12 / 3 Ans 4
print(x)
x %= 2   # x = 4 => x = 4 % 2 Ans 0
print(x)
x **= 2  # x = 0 => x = 0 ** 2 Ans 0
print(x)
x //= 2  # x = 0 => x = 0 // 2 Ans 0
print(x)

# ==================================================================

# Comparison Operators
x = 5
y = 3
print(x == y)
# returns False because 5 is not equal to 3

print(x!= y)
# returns True because 5 is not equal to 3  

print(x > y)
# returns False because 5 is not greater than 3

print(x < y)
# returns True because 5 is less than 3

print(x >= y)
# returns False because 5 is not greater than or equal to 3

print(x <= y)
# returns True because 5 is less than or equal to 3

# =================================================================
# Logical Operators

x = 5

print(x > 3 and x < 10)
# returns True because 5 is greater than 3 AND 5 is less than 10

print(x > 3 or x < 10)
# returns True because 5 is greater than 3 OR 5 is less than 10

print(not (x > 3 and x < 10))
# returns False because not (5 is greater than 3 AND 5 is less than 10) is False

# ==================================================================
# Identity Operators
# is
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have the same content

print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# is not
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)
# returns False because z is the same object as x

print(x is not y)
# returns True because x is not the same object as y, even if they have the same content

print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

# =================================================================
# Membership Operators
# is
x = ["apple", "banana"]

print("banana" in x)
# returns True because a sequence with the value "banana" is in the list

print("orange" in x)

# is not
x = ["apple", "banana"]

print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list

# =================================================================
# Bitwise Operators
print(6 & 3) # Bitwise AND

print(6 | 3) # Bitwise OR

print(6 ^ 3) # Bitwise XOR

print(~6) # Bitwise NOT

print(6 << 2) # Bitwise left shift

print(6 >> 2) # Bitwise right shift


# Python Types
print(type('Hello, world!'))  # string
print(type(13))  # integer
print(type(4.72))  # float
print(type(True))  # boolean

# Changing Types
# Moving to Integers
print(4.72, int(4.72))
print(4.05, int(4.05))

# Rounding up
print(4.72, int(4.72), int(round(4.72)))

# Moving Strings to Integers
print("12345", int("12345"))
print(type("12345"))  # string
print(type(int("12345")))  # integer
# print("Hello world", int("Hello world"))  # cannot move to integers when letters are involved

# Moving to floats
print(float(18))
print(float("12345"))

# Moving to strings
print(str(18))  # result will look like an integer but it is a string
print(str(19.5))
print(type(str(19.5)))

# Logical Operators
x = 6
print(x > 0)
print(x > 7)
print(x > 0 and x < 10)  # both most hold
print(0 < x < 10)
print(x > 0 and x < 5)

y = 24
print(y % 2 == 0)
print(y % 2 == 0 or y % 5 == 0)  # either must hold

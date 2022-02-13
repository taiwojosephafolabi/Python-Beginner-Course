# Boolean
print(type(True))  # This type is a bool
print(type("True"))  # This type is a string

# Testing whether statements are correct
print(5 == 5)
print(5 == 6)

# Incorporating if statement
x = 11
y = 5
if x % y == 0:
    print(True)
else:
    print(False)

# while loop
number = 1
while number < 4:
    print(number)
    if number == 3:
        break
    number = number + 1

# Incorporating the else statement within the while loop
number = 2
while number < 4:
    print(number)
    number = number + 1
else:
    print("number is no longer less than 4.")

# If statement
number = -10
if number >0:
    print("Positive Number")
elif number == 0:
    print("Zero")
else:
    print("Negative Number")


# Strings
print("Hello,world!")
print(type("Hello, world!"))

# Operations on Strings
# Addition sign concatenation
Greeting = "Hello"
Name = "Joseph"
print(Greeting + Name)

# * Operator
print(Name * 3)
print(Greeting + Name * 3)
print((Greeting + Name)*3)

# Index Operator
Name = "Taiwo"
print(Name[2])  # Returning the 3rd element in the list
print(Name[0] + Name[4])

# Slicing strings
print(Name[0:3])
print(Name[:2])
print(Name[3:])

# Lowercase and Uppercase
Name = "Afolabi"
print(Name.lower())
print(Name.upper())

# Count how many times a character appears in a string
print(Name.count("a"))  # only shows as 1 because a and A are different characters

# Replace specific characters with other characters
print(Name.replace("b", "m"))
New_Name = Name.replace("b", "m")
print(New_Name)

# Find the lenght of a string
Name = "Oluwagbemiga"
print(len(Name))

# Format strings
# Your_Name = input("Your name: ")
# hello = "Hello {}".format(Your_Name)
# print(hello)

# Each letter in python is assigned to a specific number
print("orange" < "strawberry")
print(ord("O"))
print(chr(78))

# In and Not Operators
fruit = "bananas"
print("a" in fruit)
print("s" not in fruit)

# Incorporate all of these
x = "hello"
y = ""
for character in x:
    y = character.upper() + y
    # y = y + character.upper()
print(y)

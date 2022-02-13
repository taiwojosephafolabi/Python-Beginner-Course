# Mini Project - Random Password Generator
# Import relevant modules
from random import randint

# All Uppercase password
password = ""  # Start with empty string
for i in range(10):  # password with 10 character
    i = chr(randint(65, 90))  # uppercase characters
    password = str(password) + i
print(password)

# Upper and Lowercase password
password = ""
for i in range(5):
    i = chr(randint(65, 90))  # uppercase characters
    for j in range(5):
        j = chr(randint(65, 90)).lower()  # lowercase characters
    password = str(password) + i + j
print(password)

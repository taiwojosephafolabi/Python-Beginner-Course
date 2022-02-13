# Tuples
# General format of tuple
Fruit = ("Apples", 4, "Bananas", 5, "Oranges", 6)  # Tuple uses round brackets
print(type(Fruit))

List_of_Fruit = ["Apples", 4, "Bananas", 5, "Oranges", 6]  # List uses square brackets
print(type(List_of_Fruit))

List_of_Fruit[0] = "Strawberries"  # Substitute element in list. Can't substitute elements in a tuple.
print(List_of_Fruit)

# Performing similar operations
# Slicing tuples
print(Fruit[0:3])
# First element
print(Fruit[0])
# Concatenation with tuples
Fruit = Fruit[0:4] + ("Cherries", 10)
print(Fruit)

# Tuple with one element
x = (5)  # not proper way
print(type(x))
y = (5, )
print(type(y))  # notation for a tuple with one element

# Length of a tuple
print(len(Fruit))

# Creating a tuple
another_tuple = tuple(("Hello", 18, True))  # Two brackets are needed.

# Converting a tuple to a list and back
Fruit = list(Fruit)
Fruit.append("Pears")
print(Fruit)  # square brackets
Fruit = tuple(Fruit)
print(Fruit)  # round brackets

# Unpacking tuples
Fruit = ("Apples", "Bananas", "Pears", "Oranges", "Strawberries")
print(len(Fruit))
(one, two, three, four, five) = Fruit  # Assign variables to the tuple
print(one)
print(two)

Fruit = ("Apples", "Bananas", "Pears", "Oranges", "Strawberries")
(one, two, *three) = Fruit  # Assign three to the last three elements in the list
print(tuple(three))

Fruit3 = ("Apples", "Bananas", "Pears", "Oranges", "Strawberries")
(one, *two, three) = Fruit # Assign three to the middle elements in the list
print(two)

# Incorporate loops within tuples
for i in range(len(Fruit)):  # If you don't know how many elements are in a tuple
    print(Fruit[i])

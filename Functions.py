# Producing function that returns x**2
def squared_number(x):
    result = x**2
    return result


print(squared_number(2))

# Two arguments
def squared_number(x, y):
    result = x**2 + y**2
    return result


print(squared_number(3, 4))

# New function (Strings)
def born(country):
    return print("I am from " + country)


born("England")

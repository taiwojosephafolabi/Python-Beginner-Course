# Define a List
my_list1 = [1, 2, 3, 4, 5, 6]
# Define a Longer List
my_list2 = list(range(1, 7))
print(my_list1)
print(my_list2)
# Lists with increments
my_list3 = list(range(1, 101, 10))
print(my_list3)
# Operations on Lists
# Returns the 1st element
print(my_list1[0])
# Returns the 3rd element
print(my_list1[2])
# Returns the last element
print(my_list1[-1])
# Create a slice from the 2nd element to the 4th element
print(my_list1[1:4])
# Length of a List
print(len(my_list3))
# Maximum and Minimum of a List
print(max(my_list3))
print(min(my_list3))
# Add an element unto list
my_list1.append(120)
print(my_list1)
# Reverse a list
my_list1.reverse()
print(my_list1)
# Add two lists together
print(my_list1 + my_list2)

# Quiz 1
# Create two variables, x=? and y=?
# where ? is any number of your choice
# Find:
# a) x plus y
# b) x divided y
# c) x minus y
# d) x multiplied by y

x = 10
y = 5

a = x + y
print("1a)", a)

b = x / y
print("1b)", b)

c = x - y
print("1c)", c)

d = x * y
print("1d)", d)

# Quiz 2
# a) Create a list of all the even numbers from 0 to 100
# b) Print the first 10 elements
# c) Find the length of the list
# d) Append a value of your choice to the end of the list

Even_Numbers = list(range(0, 101, 2))
print("2a)", Even_Numbers)
print("2b)", Even_Numbers[:10])
print("2c)", len(Even_Numbers))
Even_Numbers.append('Joseph')
print("2d)", Even_Numbers)

# Quiz 3
# a) Assign a variable to any integer
# b) Using an if statement, find whether this integer is divisible by 5

number = 9
print("3a)", number)
if number % 5 == 0:
    print("3b) Number is divisible by 5")
else:
    print("3b) Number is not divisible by 5")

# Quiz 4
# Using a for loop, get python to print numbers 0 to 5
number2 = 0
for i in range(6):
    number2 = i
    print("4)", number2)  # can just put print(i)

# Quiz 5 - Did not remember
# Draw a pentagon in turtle
import turtle

for i in range(5):
    turtle.forward(100)
    turtle.right(72)
turtle.done()

# Quiz 6
# Create a function that tests whether three numbers (a,b,c) are a Pythagorean triple
a = 5
b = 12
c = 13
def Pythagorean_Triple(a, b, c):
    if a**2 + b**2 == c**2:
        return "6) The numbers are a Pythagorean Triple"
    else:
        return "6) The numbers are a Pythagorean Triple"
print(Pythagorean_Triple(a, b, c))

# Question 7
# Spot the error
# n = 5
# while n > 0
# n = n + 1
#     print(n)

print("7) Missing indentation on line 80")
# Missing colon on line 80

# Question 8
# a) Create two lists (of size 5)
# b) Plot these lists against each other using matplotlib
import matplotlib.pyplot as plt
Year = [2018, 2019, 2020, 2021, 2022]
Trainers = [5, 2, 3, 1, 1]
plt.plot(Year, Trainers, c="cyan", linewidth=1, label="Number of Trainers", linestyle="dashed",
         marker="s", markerfacecolor="black", markersize=2)
plt.xlabel("Year")
plt.ylabel("Trainers bought")
plt.title("Trainers I bought over the years")
plt.legend()
plt.show()






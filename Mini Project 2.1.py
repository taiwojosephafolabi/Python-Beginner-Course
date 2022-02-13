import turtle
# Set-up in Turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
# Create a nice drawing
# for colours in ["red", "orange", "yellow", "green", "blue", "purple"]:
#    turtle.color(colours)
#    turtle.circle(150)
#    turtle.left(10)
# turtle.done()

# Make it cooler
for i in range(12):
    for colours in ["red", "orange", "yellow", "green", "blue", "purple"]:
        turtle.color(colours)
        turtle.circle(150)
        turtle.left(5)
turtle.done()

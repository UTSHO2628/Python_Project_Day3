import turtle

# Create the screen
screen = turtle.Screen()
screen.bgcolor("white")  # Background color

# Create a turtle object
sunflower = turtle.Turtle()
sunflower.shape("turtle")
sunflower.speed(10)  # Set speed to maximum

# Function to draw a petal
def draw_petal():
    sunflower.color("orange")  # Set the color of the petal
    sunflower.begin_fill()
    for _ in range(2):
        sunflower.circle(100, 60)  # Draw part of a circle (arc)
        sunflower.left(120)
        sunflower.circle(100, 60)
        sunflower.left(120)
    sunflower.end_fill()

# Draw the sunflower petals (8 petals)
for _ in range(8):
    draw_petal()
    sunflower.left(45)  # Rotate for the next petal

# Draw the sunflower center
sunflower.color("yellow")  # Center color
sunflower.penup()
sunflower.goto(0, -50)  # Position turtle to draw center
sunflower.pendown()
sunflower.begin_fill()
sunflower.circle(50)  # Draw the center of the sunflower
sunflower.end_fill()

# Draw the stem
sunflower.color("green")  # Set stem color
sunflower.width(5)
sunflower.penup()
sunflower.goto(0, -50)  # Position the turtle at the bottom of the flower
sunflower.pendown()
sunflower.setheading(270)  # Set direction to move downwards
sunflower.forward(200)

# Hide the turtle after drawing
sunflower.hideturtle()

# Keep the window open
turtle.done()

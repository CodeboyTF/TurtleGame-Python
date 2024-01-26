#IMPORT OUR MODULES FIRST.
import turtle

#CREATING AND INSTANCE.
pen = turtle.Turtle()

turtlestamp = turtle.Turtle()

#CREATING A STAMP() TURTLE.
turtlestamp.shape('turtle')
turtlestamp.color('green')
turtle.Screen().colormode(255)
turtle.Screen().bgcolor(29, 162, 216)
turtle.resizemode('auto')
turtlestamp.turtlesize(3, 3, 2)
turtlestamp.turtlesize(outline=3)

turtle.penup()

#CREATING THE STAMP() MOVEMENT ON THE TURTLE.
turtlestamp.backward(100)
turtlestamp.left(90)
turtlestamp.forward(100)
turtlestamp.stamp()

turtlestamp.backward(100)
turtlestamp.left(90)
turtlestamp.forward(100)
turtlestamp.stamp()

turtlestamp.backward(100)
turtlestamp.left(90)
turtlestamp.forward(100)
turtlestamp.stamp()

turtlestamp.backward(100)
turtlestamp.left(90)
turtlestamp.forward(100)
turtlestamp.stamp()

pen.hideturtle()

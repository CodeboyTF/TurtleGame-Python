#IMPORT OUR MODULES FIRST.
import turtle
import random

rainbow = turtle.Turtle()

rainbow.shape('turtle')
rainbow.penup()
turtle.colormode(255)

#MAKING DIFFERENT RAINBOW COLOURED TURTLE STAMP

# A. THIS IS THE LONGER WAY.

# rainbow.color('red')

# rainbow.stamp()
# rainbow.forward(20)
# rainbow.color('orange')

# rainbow.stamp()
# rainbow.forward(20)
# rainbow.color('yellow')

# rainbow.stamp()
# rainbow.forward(20)
# rainbow.color('green')

# rainbow.stamp()
# rainbow.forward(20)
# rainbow.color('blue')

# rainbow.stamp()
# rainbow.forward(20)
# rainbow.color('blue')

# rainbow.stamp()
# rainbow.forward(20)
# rainbow.color('pink')

# B. THIS IS THE SHORTER EFFICIENT WAY
for i in range(1):
  rainbow.stamp()
  rainbow.forward(20)
  rainbow.color('red')
  rainbow.stamp()
  rainbow.forward(20)
  rainbow.color('orange')
  rainbow.stamp()
  rainbow.forward(20)
  rainbow.color('yellow')
  rainbow.stamp()
  rainbow.forward(20)
  rainbow.color('green')
  rainbow.stamp()
  rainbow.forward(20)
  rainbow.color('purple')
  rainbow.stamp()
  rainbow.forward(20)
  rainbow.color('blue')
  rainbow.stamp()
  rainbow.forward(20)
  rainbow.color('pink')

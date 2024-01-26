
#IMPORT OUR MODULES FIRST.
import turtle

#CREATING OUR TURTLE AND THE SCREEN.
turtle.shape('turtle')
turtle.setup(500, 500)
turtle.penup()
turtle.Screen().colormode(255)
turtle.Screen().bgcolor(29, 162, 216)

#CREATING COLOR ON THE TURTLE.
turtle.color(9, 185, 13)
turtle.pencolor(0, 128, 0)
turtle.resizemode('auto')
turtle.turtlesize(3, 3, 2)
turtle.turtlesize(outline=3)

#MAKING OUR TURTLE MOVE IN DIFFERENT DIRECTION.
for i in range(4):
  turtle.forward(200)
  turtle.left(90)
  turtle.forward(200)
  turtle.left(90)
  turtle.forward(200)
  turtle.left(90)







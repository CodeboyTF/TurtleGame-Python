#IMPORT OUR MODULES FIRST.
import turtle
import random

stamp = turtle.Turtle()

stamp.shape('turtle')
# stamp.setup(500, 500)
stamp.penup()
turtle.colormode(255)

paces = 50
random_red = 255
random_green = 255
random_blue = 255

for i in range(50):
  random_red= random.randint(0, 255)
  random_green = random.randint(0, 255)
  random_blue = random.randint(0, 255)

stamp.color(random_red, random_blue, random_green)

paces += 3
# A

# stamp.stamp()
# stamp.forward(paces)
# stamp.right(25)

# stamp.stamp()
# stamp.forward(paces)
# stamp.right(25)

# stamp.stamp()
# stamp.forward(paces)
# stamp.right(25)
# stamp.stamp()
# stamp.forward(paces)
# stamp.right(25)
# stamp.stamp()
# stamp.forward(paces)
# stamp.right(25)
# stamp.stamp()
# stamp.forward(paces)
# stamp.right(25)
# stamp.stamp()
# stamp.forward(paces)
# stamp.right(25)
# stamp.stamp()
# stamp.forward(paces)
# stamp.right(25)
# stamp.stamp()
# stamp.forward(paces)
# stamp.right(25)
# stamp.stamp()
# stamp.forward(paces)
# stamp.right(25)
# stamp.stamp()
# stamp.forward(paces)
# stamp.right(25)


#CHOOSE BETWEEN THE TWO: A OR B

# B
for j in range(50):
  stamp.stamp()
  stamp.forward(paces)
  stamp.right(25)


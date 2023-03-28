import turtle
import math
# square with diagonals
turtle.reset()
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.left(45)
turtle.forward(100 * math.sqrt(2))
turtle.left(135)
turtle.forward(100)
turtle.left(135)
turtle.forward(100 * math.sqrt(2))
# diagonals
turtle.up()
turtle.left(45)
turtle.forward(250)
turtle.down()
turtle.left(135)
turtle.forward(100 * math.sqrt(2))
turtle.left(135)
turtle.up()
turtle.forward(100)
turtle.down()
turtle.left(135)
turtle.forward(100 * math.sqrt(2))
# square
turtle.left(135)
turtle.up()
turtle.forward(550)
turtle.left(90)
turtle.forward(100)
turtle.down()
turtle.left(30)
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
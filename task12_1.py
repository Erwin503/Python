import turtle
turtle.reset()
turtle.left(180)
turtle.color('Yellow')
for i in range(3):
    turtle.right(120)
    turtle.forward(50)
turtle.up()
turtle.forward(100)
turtle.down()
turtle.begin_fill()
for i in range(3):
    turtle.right(120)
    turtle.forward(50)
turtle.end_fill()
turtle.up()
turtle.forward(100)
turtle.down()
turtle.color('Red')
for i in range(3):
    turtle.right(120)
    turtle.forward(50)
turtle.begin_fill()
turtle.end_fill()

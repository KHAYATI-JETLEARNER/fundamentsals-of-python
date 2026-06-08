import turtle

pen = turtle.Turtle()
pen.speed(10)
paper = turtle.Screen()

for i in range(4):
    pen.forward(40)
    pen.left(90)

pen.up()
pen.goto(40, 40)
pen.down()

for i in range(4):
    pen.forward(40)
    pen.left(90)

turtle.done()





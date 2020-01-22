import turtle
ico=turtle.Turtle()
ico.speed()
ico.color("red")
screen=turtle.Screen()

screen.bgcolor("black")
ico.begin_fill()
ico.pensize(4)
for i in range(8):

    ico.forward(200)
    for i in range(12):
        ico.right(30)
        ico.forward(40)
        ico.dot(18,'orange')
        ico.backward(40)


    ico.backward(100)
    ico.left(45)



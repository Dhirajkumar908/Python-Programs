import turtle
nishi=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor("black")
#nishi.penup(100,100)
colors=["red","green","blue","yellow","white"]
turtle.Screen()
nishi.speed(50)
nishi.color("green")

#nishi.circle(20)
#nishi.goto(0,100)
for i in range(1000):
    nishi.forward(i*4+10)
    nishi.pensize(i*2)

    nishi.right(59)
    nishi.pencolor(colors[i%5])
   # nishi.circle(50)
    nishi.pencolor(colors[i%5])




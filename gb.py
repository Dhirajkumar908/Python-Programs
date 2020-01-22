import turtle
d=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor("white")
d.pensize(15)
colors = ["purple","blue","red"]
d.speed(99)
for i in range(500):
  #  d.color("green","red")
    d.pencolor(colors[i % 3])
    d.circle(80)
    #d.pinup(50)
    d.circle(80)
    d.right(140)
   # d.forward(i*3+5)
   # d.circle(100)
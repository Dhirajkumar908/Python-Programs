import turtle
pen=turtle.Turtle()
pen=turtle.Screen()
colors = [ "red","purple","blue","green","orange","yellow"]
pen = turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
   pen.pencolor(colors[x % 6])
   pen.width(x/100 + 1)
   pen.forward(x)
   pen.left(59)
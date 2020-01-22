import turtle as t
t.speed(2000)
t.pensize(3)

colors = ["purple","blue","red"]

t.left(90)
t.backward(100)
t.color("green")

def draw(l):
    if(l<15):
        return
    else:
        t.forward(l)
        t.color("yellow")
        t.circle(3)
        t.color("green")
        t.left(30)
        draw(5*l/6)
        t.right(60)
        draw(5*l/6)
        t.left(30)
        t.backward(l)

draw(120)
t.exitonclick()
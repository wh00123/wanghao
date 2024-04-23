import turtle as t

t.speed(10)

t.penup()
t.sety(100)
t.pendown()

t.bgcolor('red')
t.color("yellow", 'yellow')

t.begin_fill()
t.right(72)
t.fd(100)

i = 1
while i <= 4:
    t.left(72)
    t.fd(100)
    t.right(144)
    t.fd(100)
    i += 1

t.left(72)
t.fd(100)
t.end_fill()

t.hideturtle()

t.done()

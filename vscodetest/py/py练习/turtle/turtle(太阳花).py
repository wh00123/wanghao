import turtle as t
i = 1

t.penup()
t.setx(200)
t.pendown()

t.speed(10)
t.color("red", "yellow")
t.begin_fill()
while i <= 36:
    t.left(170)
    t.fd(400)
    i += 1

t.end_fill()

t.done()

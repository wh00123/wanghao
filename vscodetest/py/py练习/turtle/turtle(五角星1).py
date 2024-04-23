import turtle as t

t.setup(1600, 1300)

t.bgcolor('red')

t.speed(10)

t.color('blue', 'blue')
t.begin_fill()
t.circle(-280)
t.end_fill()

t.color("red", "yellow")

t.begin_fill()
t.goto(80, -180)  # 1
t.goto(260, -180)  # 2
t.goto(130, -300)  # 3
t.goto(170, -500)  # 4
t.goto(0, -380)  # 5/-5
t.goto(-170, -500)  # -4
t.goto(-130, -300)  # -3
t.goto(-260, -180)  # -2
t.goto(-80, -180)  # -1
t.goto(0, 0)
t.end_fill()

t.done()

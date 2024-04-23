# 奥运五环
import turtle as t

t.pensize(5)

# 蓝圆
t.penup()
t.right(90)
t.forward(-50)
t.left(90)
t.forward(-200)
t.pendown()
t.pencolor("blue")
t.circle(100)

# 黑圆
t.penup()
t.forward(250)
t.pendown()
t.pencolor("black")
t.circle(100)

# 红圆
t.penup()
t.forward(250)
t.pendown()
t.pencolor("red")
t.circle(100)

# 黄圆
t.penup()
t.forward(-275)
t.right(-90)
t.pendown()
t.pencolor("yellow")
t.circle(100)

# 绿圆
t.penup()
t.left(-90)
t.forward(50)
t.right(90)
t.pendown()
t.pencolor("green")
t.circle(100)

t.done()

import turtle as t
t.pensize(6)  # 调整笔大小

# 设置笔颜色和填充颜色
t.color('black', 'red')

t.begin_fill()  # 开始填充
t.circle(50)

# 移动笔
t.penup()  # 抬笔
t.fd(100)
t.pendown()  # 落笔

t.circle(50)
t.end_fill()  # 结束填充

t.done()  # 结束绘画

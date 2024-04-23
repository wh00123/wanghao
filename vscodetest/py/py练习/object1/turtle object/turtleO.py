import turtle as t


class turtleO:
    radis = 0
    radian = 0
    color = "black"
    fillcolor = "yellow"

    def __init__(self, radis, radian, color, fillcolor):
        self.radis = radis
        self.radian = radian
        self.color = color
        self.fillcolor = fillcolor

    def circle1(self, radis, radian, color, fillcolor):
        t.pencolor(self.color)
        t.fillcolor(self.fillcolor)
        t.begin_fill()
        t.circle(self.radis, self.radian)
        t.end_fill()
        # t.done

    def goto(self, x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()


if __name__ == '__main__':
    r = int(input('半径'))
    h = int(input('弧长'))
    color = input('画笔颜色')
    fillcolor = input('填充颜色')
    t1 = turtleO(r, h, color, fillcolor)
    t1.circle1(t1.radis, t1.radian, t1.color, t1.fillcolor)
    x1 = int(input())
    y1 = int(input())
    t.radian = 180
    t1.goto(x1, y1)
    t1.circle1(t1.radis, t1.radian, t1.color, t1.fillcolor)
    t.done()

turtleO()
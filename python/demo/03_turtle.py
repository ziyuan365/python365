import turtle

#创建turtle对象
t=turtle.Turtle()

#设置画布大小
turtle.setup(500,500)
#设置背景颜色
turtle.bgcolor("green")
#设置笔的粗细和颜色
t.pensize(5)
t.pencolor("black")
t.write("hello turtle")
#绘制圆形
t.penup()
t.goto(-75,50)
t.pendown()
t.circle(50)
#绘制长方形
t.penup()
t.goto(-25,-50)
t.pendown()
t.pensize(3)
t.pencolor("blue")
for i in range(2):
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)

#保持窗口常开
turtle.done()
import turtle as t
t.setup(650,350,0,0)
t.color('red')
t.pensize(2)
t.penup()
t.fd(-250)
t.goto(-250,150)
t.fd(100)
t.pendown()
for i in range(2):
    t.circle(-80,80)
t.seth(-30)
for i in range(2):
    t.circle(-80,80)
t.seth(-90)
t.fd(10)
t.seth(0)
t.fd(2)
for i in range(2):
    t.circle(80,80)
t.seth(30)
t.fd(10)
for i in range(2):
    t.circle(80,80)
t.seth(90)
t.fd(5)
t.seth(0)
t.fd(60)
t.done()

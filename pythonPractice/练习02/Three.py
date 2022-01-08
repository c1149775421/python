import turtle as t
t.setup(650,350,0,0)
t.color('red')
t.pensize(30)
t.penup()
t.fd(-250)
t.goto(-250,150)
t.fd(100)
t.pendown()
for i in range(2):
    t.circle(-80,80)
t.seth(-25)
t.fd(10)
for i in range(2):
    t.circle(-80,80)
t.done()

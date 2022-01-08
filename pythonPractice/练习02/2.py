import turtle as t
t.setup(650,550,0,0)
t.penup()
t.fd(-100)
t.pendown()
t.pensize(5)
t.pencolor("red")
for i in range(1):
    t.circle(150)

for n in range(1):
    t.penup()
    t.goto( -100, 100)
    t.pendown()
    t.circle(30)


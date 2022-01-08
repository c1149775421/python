import turtle as t
t.pensize(2)
for i in range(4):
    t.seth(90*i)
    t.fd(80)
    t.right(45)
    t.circle(-80,80)
    t.goto(0,0)
   

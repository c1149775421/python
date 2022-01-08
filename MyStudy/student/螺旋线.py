import turtle as t
import time
t.speed("fastest")
t.pensize(2)
for i in range(100):
    t.forward(2*i)
    t.left(90)
time.sleep(3)

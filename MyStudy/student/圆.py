import turtle as t
t.color('blue', 'red')
t.begin_fill()
while True:
    t.forward(30)
    t.right(15)
    if abs(t.pos()) < 1:
        break
t.end_fill()
done()

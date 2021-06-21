import turtle, time


def drawgap():
    turtle.penup()
    turtle.fd(5)


def drawline(draw):
    drawgap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawgap()
    turtle.right(90)


def drawdigit(digit):
    drawline(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 2, 6, 8] else drawline(False)
    turtle.left(90)
    drawline(True) if digit in [0, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)


def drawdate(date):
    turtle.pencolor('red')
    for i in date:
        if i == '-':
            turtle.write('月', font=('Arial', 18, 'normal'))
            turtle.pencolor('green')
            turtle.fd(40)
        elif i == '=':
            turtle.write('号', font=('Arial', 18, 'normal'))
            turtle.pencolor('purple')
            turtle.fd(40)
        elif i == '+':
            turtle.write('时', font=('Arial', 18, 'normal'))
            turtle.pencolor('brown')
            turtle.fd(40)
        elif i == '!':
            turtle.write('分', font=('Arial', 18, 'normal'))
            turtle.fd(40)
        elif i == '*':
            turtle.write('秒', font=('Arial', 18, 'normal'))
            turtle.fd(40)
        else:
            drawdigit(eval(i))


def main():
    turtle.setup(1000, 350, 200, 200)
    turtle.pensize(5)
    turtle.speed(0)
    while True:
        turtle.clear()
        turtle.penup()
        turtle.setpos(-400, 0)
        # turtle.penup()
        # turtle.fd(-300)
        # print(turtle.pos())
        drawdate(time.strftime('%m-%d=%H+%M!%S*', time.gmtime()))
        turtle.hideturtle()
        time.sleep(5)
    # drawdate(time.strftime('%Y-%m=%d+'))

    turtle.done()


if __name__ == "__main__":
    main()


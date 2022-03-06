import turtle

# t = turtle.Turtle()


def drawTree(branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        drawTree(branch_len - 15)
        t.left(40)
        drawTree(branch_len - 15)
        t.right(20)
        t.backward(branch_len)


# t.left(90)
# t.penup()
# t.backward(100)
# t.pendown()
# t.pencolor('green')
# drawTree(100)
# turtle.done()


def siepinski(degree, points):
    colormap = ['blue', 'red', 'green', 'pink', 'white', 'yellow']
    drawTriangle(points, colormap[degree])
    if degree > 0:
        siepinski(degree - 1, {
            'left': points['left'],
            'top': getMid(points['left'], points['top']),
            'right': getMid(points['left'], points['right'])
        })
        siepinski(degree - 1, {
            'left': getMid(points['left'], points['top']),
            'top': points['top'],
            'right': getMid(points['top'], points['right'])
        })
        siepinski(degree - 1, {
            'left': getMid(points['left'], points['right']),
            'top': getMid(points['right'], points['top']),
            'right': points['right']
        })


def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def drawTriangle(points, color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()


# points = {
# 'left' : (-200,-100),
# 'top' : (0,200),
# 'right' : (200,-100)
# }
# siepinski(5,points)
# turtle.done()


def moveTower(height, fromPole, withPole, toPole):
    if height >= 1:
        moveTower(height-1,fromPole,toPole,withPole)
        moveDisk(height,fromPole,toPole)
        moveTower(height - 1, withPole, fromPole, toPole)

def moveDisk(disk,fromPole,toPole):
    print("Moving disk[{}] from {} to {}".format(disk,fromPole,toPole))

moveTower(5,'#1','#2','#3')



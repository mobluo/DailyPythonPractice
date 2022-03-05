import turtle
def drawTree(branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        drawTree(branch_len-15)
        t.left(40)
        drawTree(branch_len - 15)
        t.right(20)
        t.backward(branch_len)

t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor('green')
drawTree(100)
turtle.done()
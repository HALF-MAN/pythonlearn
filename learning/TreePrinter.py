import turtle
from random import *
def printer(depth):
    if depth > 0:
        len = randint(40, 80)
        turtle.fd(len)
        randAng = randint(25, 45)
        turtle.right(randAng)
        printer(depth-1)

        turtle.left(randAng*2)
        printer(depth-1)

        turtle.right(randAng)
        turtle.backward(len)

def draw_branch(branch_length):
    if branch_length > 5:           #限定绘制的树枝(包括树干、树枝和树叶)长度至少大于5
        if(branch_length<=20):      #如果长度小于20，即可判定是树叶,绘制成绿色
            turtle.color('green')
        else:
            turtle.color('brown')

        turtle.forward(branch_length)       #绘制树干
        randAng = randint(15, 25)
        turtle.right(randAng)
        draw_branch(branch_length-15)       #绘制每个节点分叉右侧的树枝

        turtle.left(randAng*2)
        draw_branch(branch_length - 15)     #绘制每个节点分叉左侧的树枝

        if (branch_length > 20):    #如果长度大于20，即可判定是树干或者树枝，绘制成棕色
            turtle.color('brown')
        turtle.right(randAng)
        turtle.backward(branch_length)
def main():
    turtle.setup(800, 800, 200, 200)
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pensize(5)
    turtle.pendown()
    turtle.left(90)
    turtle.fd(100)
    draw_branch(80)
    # printer(3)
    turtle.done()
main()
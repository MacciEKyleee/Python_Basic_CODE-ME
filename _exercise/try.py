import turtle
# from turtle import *
# turtle.hideturtle()
# turtle.textinput('Wisielec','Krok')

def etap_1(zolw):
    zolw.forward(50)
    zolw.backward(100)
    zolw.forward(50)
    zolw.left(90)
    zolw.forward(200)
    zolw.right(90)
    zolw.forward(50)

def etap_2(zolw):



def main():
    t = turtle.Turtle()
    etap_2(t)
    turtle.done()


# step 0
turtle.right(90)
turtle.forward(30)
# step 1
turtle.right(90)
turtle.circle(15, 540)
# step 2
turtle.right(90)
turtle.forward(20)
# step 3
turtle.right(30)
turtle.forward(40)
turtle.backward(40)
# step 4
turtle.left(60)
turtle.forward(40)
turtle.backward(40)
# step 5
turtle.right(30)
turtle.forward(55)
# step 6
turtle.right(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(40)
turtle.backward(40)
turtle.left(90)
turtle.forward(10)
# step 7
turtle.forward(10)
turtle.right(90)
turtle.forward(40)

#turtle.bgcolor('red')
#hideturtle()
#end_fill()
#turtle.end_fill('red')
turtle.colormode(255)
print('You are dead !')


turtle.done()

if __name__ == '__main__':
    main()


import turtle

def etap_1(zolw):
    zolw.forward(200)

def etap_2(zolw):
    etap_1(zolw)
    zolw.backward(100)
    zolw.left(90)
    zolw.forward(300)



def main():
    t = turtle.Turtle()
    etap_2(t)
    turtle.done()

if __name__ == '__main__':
    main()
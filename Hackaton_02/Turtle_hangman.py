import turtle
# from turtle import *
# turtle.hideturtle()
# turtle.textinput('Wisielec','Krok')

def etap_1(zolw):
    zolw.hideturtle()
    zolw.forward(50)
    zolw.backward(100)
    zolw.forward(50)
    zolw.left(90)
    zolw.forward(200)
    zolw.right(90)
    zolw.forward(50)

def etap_2(zolw):
    zolw.hideturtle()
    etap_1(zolw)
    zolw.right(90)
    zolw.forward(30)

def etap_3(zolw):
    zolw.hideturtle()
    etap_2(zolw)
    zolw.right(90)
    zolw.circle(15, 540)

def etap_4(zolw):
    zolw.hideturtle()
    etap_3(zolw)
    zolw.right(90)
    zolw.forward(20)

def etap_5(zolw):
    zolw.hideturtle()
    etap_4(zolw)
    zolw.right(30)
    zolw.forward(40)
    zolw.backward(40)

def etap_6(zolw):
    zolw.hideturtle()
    etap_5(zolw)
    zolw.left(60)
    zolw.forward(40)
    zolw.backward(40)

def etap_7(zolw):
    zolw.hideturtle()
    etap_6(zolw)
    zolw.right(30)
    zolw.forward(55)

def etap_8(zolw):
    zolw.hideturtle()
    etap_7(zolw)
    zolw.right(90)
    zolw.forward(10)
    zolw.left(90)
    zolw.forward(40)
    zolw.backward(40)
    zolw.left(90)
    zolw.forward(10)

def etap_9(zolw):
    zolw.hideturtle()
    zolw.color("red")
    zolw.pensize(3)

    etap_8(zolw)
    zolw.forward(10)
    zolw.right(90)
    zolw.forward(40)

   # zolw.write('You are dead !')
    print('You are dead !')


def main():
    t = turtle.Turtle()
    etap_9(t)
    turtle.done()

if __name__ == '__main__':
    main()



#turtle.bgcolor('red')
#hideturtle()
#end_fill()
#turtle.end_fill('red')

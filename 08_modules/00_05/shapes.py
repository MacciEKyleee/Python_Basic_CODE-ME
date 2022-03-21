'''
modul including calculation of shapes areas
'''

# def type():
#     v = input('Podaj jaki kształt ma pokój')
#
# def ares():

def square(a):
    return a*a

def triangle(a,h):
    return (a*h*0.5)

def rectangle(a,b):
    return a*b

def circle(r):
    return 3.14*r*r

def trapezoid(a,b,h):
    return (a+b)*h*0.5
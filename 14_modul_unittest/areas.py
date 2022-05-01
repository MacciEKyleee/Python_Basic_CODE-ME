def check(v):
    if not(isinstance(a,(inf,float))):
        raise ValueError('Bok musi być wartością numeryczną!')
def square(a):
    check(a)
    return a * a

def triangle(a,h):
    check(a)
    check(h)
    return a * h

def rectangle(a, b):
    # if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
    #     raise ValueError('Bok musi być wartością numeryczną!')
    check(a)
    check(b)
    return a * b


# def triangle(a,h):
#     if not(isinstance(a,(int,float))) and isinstance(b,(int,float)):
#         raise ('Bok musi być wartością numeryczną!')
#    #try:
#         # if int(a) and int(b):
#         #     return a*b
#         #return float(a)*float(b)
#
#
#     return (a*h*0.5)

# def rectangle(a, b):
#     return a * b


def circle(r):
    check(r)
    return 3.14 * r * r


def trapezoid(a, b, h):
    check(a)
    check(b)
    check(h)
    return (a + b) * h * 0.5

"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector


def line(start, end):
    color('blue', 'red')
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    import turtle
    color('black', 'pink')
    """Draw square from start to end."""
    
    turtle.goto (175, 100)
    turtle.color ("purple", "yellow")
    turtle.pendown ()
    turtle.begin_fill()

    for i in range (4):
        turtle.forward(150)
        turtle.left(90)
    turtle.end_fill ()


def circulo(start, end):
    """Draw circle from start to end."""
    import turtle
    turtle.color ("black", "pink")
    draw = turtle.Turtle ()
    draw.circle(140)


def rectangle(start, end):
    """Draw rectangle from start to end."""
    import turtle
    turtle.color ("blue", "white")


def triangle(start, end):
    """Draw triangle from start to end."""
    import turtle
    turtle.color ("red", "yellow")


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circulo), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()

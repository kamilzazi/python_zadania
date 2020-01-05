"""Korzystając z modułu turtle narysujcie coś takiego:
https://pythonalx.slack.com/files/UDMCSAVJR/FRYD5KTA7/image.png"""


import turtle
adam = turtle.Turtle()

y = 50
x = 250
while x > 0:
    adam.left(90)
    adam.forward(y)
    adam.left(90)
    adam.forward(x)
    adam.left(90)
    adam.forward(y)
    adam.left(90)
    adam.forward(x)
    y += 50
    x -= 50
turtle.done()
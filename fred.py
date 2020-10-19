Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> fred = turtle.Pen()
>>> fred.shape("turtle")
>>> fred.colour("green")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    fred.colour("green")
AttributeError: 'Turtle' object has no attribute 'colour'
>>> fred.color("green")
>>> fred.forward(100)
>>> fred.left(90)
>>> fred.forward(100)
>>> fred.left(90)
>>> fred.forward(100)
>>> fred.left(90)
>>> fred.forward(100)
>>> fred.circle(100)
>>> 
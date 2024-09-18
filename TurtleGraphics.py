#TurtleGraphics.py
#Name: Logan Baardson
#Date: 9/18
#Assignment: Turtle graphics

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(myTurtle, sides):
    for i in range(sides):
     myTurtle.forward(50)
     myTurtle.right(360/sides)

def fillCorner(myTurtle, corner):
    drawSquare(myTurtle, 100)
    if corner == 1:
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
    if corner == 2:
        myTurtle.up()
        myTurtle.goto(50,0)
        myTurtle.down()
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
    if corner == 3:
        myTurtle.up()
        myTurtle.goto(50,-50)
        myTurtle.down()
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
    if corner == 4:
        myTurtle.up()
        myTurtle.goto(0,-50)
        myTurtle.down()
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
        
def squaresInSquares(myTurtle, num):
    size = 10
    for i in range(num):
        myTurtle.up()
        myTurtle.goto((-size/2),(size/2))
        myTurtle.down()
        drawSquare(myTurtle, size)
        size = size + 20
        
def main():
    myTurtle = turtle.Turtle()
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    #squaresInSquares(myTurtle, 100) #draws 5 concentric squares
    #squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()

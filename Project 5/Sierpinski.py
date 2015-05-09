import turtle
from Tkinter import *
import canvasvg

def drawTriangle(points,color,Turt):
    Turt.fillcolor(color)
    Turt.up()
    
    Turt.goto(points[0][0],points[0][1])
    Turt.down()
    
    Turt.begin_fill()
    
    Turt.goto(points[1][0],points[1][1])
    Turt.goto(points[2][0],points[2][1])
    Turt.goto(points[0][0],points[0][1])
    
    Turt.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def Striangle(points,degree,Turt):
    colormap = ['black','gray','white','white','grey',
                'white','white']
    
    drawTriangle(points,colormap[degree],Turt)
    
    if degree > 0:
        Striangle([points[0], getMid(points[0], points[1]),
                        getMid(points[0], points[2])], degree-1, Turt)
    
        Striangle([points[1], getMid(points[0], points[1]),
                        getMid(points[1], points[2])], degree-1, Turt)
        
        Striangle([points[2], getMid(points[2], points[1]),
                        getMid(points[0], points[2])], degree-1, Turt)

def main():
   
   Turt = turtle.Turtle()
   
   #turtle.screensize(800, 800)
   
   Turt.tracer(0, 0)
   myWin = turtle.Screen()
   
   Pnts = [[-300,-200],[0,300],[300,-200]]
   
   Striangle(Pnts,6,Turt)
   ts = turtle.getscreen()
   
   #ts.getcanvas().postscript(file="SierpinskiTriangle.svg")
   #ts.getcanvas().postscript(file="SierpinskiTriangle.png")
   #ts.getcanvas().postscript(file="SierpinskiTriangle.jpg")
   #ts.getcanvas().postscript(file="SierpinskiTriangle.eps")

   #canvasvg.saveall("SierpinskiT.svg", Turtle._canvas)
   myWin.exitonclick()

main()
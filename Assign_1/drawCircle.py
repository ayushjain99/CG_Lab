# Mid-Point Circle Generation Algorithm
# Ayush Jain - 2017UCP1168
window = (0,0,0,0)
viewport = (0,0,0,0)
from graphics import *
import math
import time

def transform(xw,yw):
    # print(window)
    # print(viewport)
    (xw_min,yw_min,xw_max,yw_max) = window
    (xv_min,yv_min,xv_max,yv_max) = viewport
    xv = (xw - xw_min)/(xw_max - xw_min)
    xv = xv*(xv_max - xv_min)
    xv = xv + xv_min
    xv = round(xv)
    yv = (yw - yw_min)/(yw_max - yw_min)
    yv = yv*(yv_max - yv_min)
    yv = yv + yv_min
    yv = yv_max - yv
    yv = round(yv)
    return Point(xv,yv)

def circlePoints(x,y,a,b,color,win):
    pt = transform(x+a,y+b)
    win.plotPixel(pt.getX(),pt.getY(),color)
    pt = transform(y+a,x+b)
    win.plotPixel(pt.getX(),pt.getY(),color)
    pt = transform(-x+a,y+b)
    win.plotPixel(pt.getX(),pt.getY(),color)
    pt = transform(-y+a,x+b)
    win.plotPixel(pt.getX(),pt.getY(),color)
    pt = transform(-y+a,-x+b)
    win.plotPixel(pt.getX(),pt.getY(),color)
    pt = transform(-x+a,-y+b)
    win.plotPixel(pt.getX(),pt.getY(),color)
    pt = transform(y+a,-x+b)
    win.plotPixel(pt.getX(),pt.getY(),color)
    pt = transform(x+a,-y+b)
    win.plotPixel(pt.getX(),pt.getY(),color)

def plotCircle(a,b,R,win):
    x = 0 ; y = R
    d = 1-R ; x_final = int(round(0.7071*R))
    while(x <= x_final):
        circlePoints(x,y,a,b,"black",win)
        # time.sleep(0.2)
        if(d<0):
            # Choose E
            d = d + 2*x + 3
        else:
            y = y - 1
            d = d + 2*(x-y) + 5
        x += 1

def main():
    global viewport,window
    print("Enter length of viewport : ",end="") ; x = int(input())
    print("Enter width of viewport : ",end="") ; y = int(input())
    # Notation : viewport = (xv_min,yv_min,xv_max,yv_max)
    viewport = (0,0,x,y)
    win = GraphWin("Scan Conversion of Circles",x,y)
    win.setBackground(color_rgb(255, 165, 0))
    print("Enter xw_min : ",end="") ; xw_min = int(input())
    print("Enter yw_min : ",end="") ; yw_min = int(input())
    print("Enter xw_max : ",end="") ; xw_max = int(input())
    print("Enter yw_max : ",end="") ; yw_max = int(input())
    # Some Sanity Checks for window corners
    if(xw_min>xw_max):
        (xt,yt) = (xw_min,yw_min)
        (xw_min,yw_min) = (xw_max,yw_max)
        (xw_max,yw_max) = (xt,yt)
    if(yw_min>yw_max):
        (yw_min,yw_max) = (yw_max,yw_min)
    win.setCoords(xw_min,yw_min,xw_max,yw_max)
    # Notation : window = (xw_min,yw_min,xw_max,yw_max)
    window = (xw_min,yw_min,xw_max,yw_max)
    print("Enter centre of circle(x space y) : ",end="")
    (x0,y0) = (map(int,input().split()))
    print("Enter radius of circle : ",end="")
    R = int(input())
    plotCircle(x0,y0,R,win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()

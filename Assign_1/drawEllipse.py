# Mid-Point Ellipse Drawing Algorithm
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

def ellipsePoints(x,y,a,b,color,win):
    pt = transform(x+a,y+b)
    win.plotPixel(pt.getX(),pt.getY(),color)
    pt = transform(-x+a,y+b)
    win.plotPixel(pt.getX(),pt.getY(),color)
    pt = transform(x+a,-y+b)
    win.plotPixel(pt.getX(),pt.getY(),color)
    pt = transform(-x+a,-y+b)
    win.plotPixel(pt.getX(),pt.getY(),color)

def plotEllipse(a,b,x0,y0,win):
    x = 0 ; y = b;
    # Initialize decision parameter for Region 1
    d1 = (b*b) - (a*a*b) + (0.25*a*a)
    dx = 2*b*b*x
    dy = 2*a*a*y
    # For Region 1
    while (dx < dy):
        ellipsePoints(x,y,x0,y0,"black",win)
        if (d1 < 0):
            dx = dx + (2 * b * b)
            d1 = d1 + dx + (b * b)
        else:
            y=y-1;
            dx = dx + (2 * b * b)
            dy = dy - (2 * a * a)
            d1 = d1 + dx - dy + (b * b)
        x=x+1

    # Decision parameter for Region 2
    d2 = ((b * b) * ((x + 0.5) * (x + 0.5))) + \
    ((a * a) * ((y - 1) * (y - 1))) - \
    (a * a * b * b)
    # Plotting points of Region 2
    while (y >= 0):
        ellipsePoints(x,y,x0,y0,"black",win)
        if (d2 > 0):
            dy = dy - (2 * a * a)
            d2 = d2 + (a * a) - dy
        else:
            x=x+1
            dx = dx + (2 * b * b)
            dy = dy - (2 * a * a)
            d2 = d2 + dx - dy + (a * a)
        y=y-1

def main():
    global viewport,window
    print("Enter length of viewport : ",end="") ; x = int(input())
    print("Enter width of viewport : ",end="") ; y = int(input())
    # Notation : viewport = (xv_min,yv_min,xv_max,yv_max)
    viewport = (0,0,x,y)
    win = GraphWin("Scan Conversion of Ellipse",x,y)
    win.setBackground(color_rgb(195, 141, 158))
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
    print("Enter center of ellipse(x space y) : ",end="")
    (x0,y0) = (map(int,input().split()))
    print("Enter semi-major axis of ellipse : ",end="")
    a = int(input())
    print("Enter semi-minor axis of ellipse : ",end="")
    b = int(input())
    plotEllipse(a,b,x0,y0,win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()

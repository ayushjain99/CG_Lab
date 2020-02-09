# Bresenham Mid-Point Line Generation Algorithm
# Ayush Jain - 2017UCP1168
window = (0,0,0,0)
viewport = (0,0,0,0)
from graphics import *

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

# We have to handle all cases -> all quadrants,negative slopes
# horizontal lines, vertical lines
def plotLine(x0,y0,x1,y1,win):
    # Take care of vertical line separately and
    # rest other cases using reflection
    if(x1-x0 == 0):
        slope = None
        (x0,y0) = (y0,x0)
        (x1,y1) = (y1,x1)
    else:
        slope = (y1-y0)/(x1-x0)
        if(slope >= 0) and (abs(slope) > 1):
            (x0,y0) = (y0,x0)
            (x1,y1) = (y1,x1)
        elif(slope < 0) and (abs(slope) <= 1):
            (x0,y0) = (-x0,y0)
            (x1,y1) = (-x1,y1)
        elif(slope < 0) and (abs(slope) > 1):
            (x0,y0) = (y0,-x0)
            (x1,y1) = (y1,-x1)
    if(x0 > x1):
        (xt,yt) = (x0,y0)
        (x0,y0) = (x1,y1)
        (x1,y1) = (xt,yt)
    # Now the actual algorithm with those assumptions
    dy = y1 - y0 ; dx = x1 - x0
    a = dy ; b = -dx
    delta_E = a ; delta_NE = a + b
    # Initialize d (decision parameter)
    d = a + (b/2)
    x = x0 ; y = y0
    print("Slope =",slope)
    while(x <= x1):
        if(slope is None):
            (xp,yp) = (y,x)
        elif(slope >= 0) and (abs(slope) > 1):
            (xp,yp) = (y,x)
        elif(slope < 0) and (abs(slope) <= 1):
            (xp,yp) = (-x,y)
        elif(slope < 0) and (abs(slope) > 1):
            (xp,yp) = (-y,x)
        else:
            (xp,yp) = (x,y)
        pt = transform(xp,yp)
        win.plotPixel(pt.getX(),pt.getY(),"black")
        if(d<0):
            # Choose East
            d = d + delta_E
        else:
            d = d + delta_NE
            y = y + 1
        x = x + 1

def main():
    global viewport,window
    print("Enter length of viewport : ",end="") ; x = int(input())
    print("Enter width of viewport : ",end="") ; y = int(input())
    # Notation : viewport = (xv_min,yv_min,xv_max,yv_max)
    viewport = (0,0,x,y)
    win = GraphWin("Bresenham Line Generation",x,y)
    win.setBackground(color_rgb(60, 179, 113))
    print("Enter xw_min : ",end="") ; xw_min = int(input())
    print("Enter yw_min : ",end="") ; yw_min = int(input())
    print("Enter xw_max : ",end="") ; xw_max = int(input())
    print("Enter yw_max : ",end="") ; yw_max = int(input())
    if(xw_min>xw_max):
        (xt,yt) = (xw_min,yw_min)
        (xw_min,yw_min) = (xw_max,yw_max)
        (xw_max,yw_max) = (xt,yt)
    if(yw_min>yw_max):
        (yw_min,yw_max) = (yw_max,yw_min)
    win.setCoords(xw_min,yw_min,xw_max,yw_max)
    # Notation : window = (xw_min,yw_min,xw_max,yw_max)
    window = (xw_min,yw_min,xw_max,yw_max)
    print("Enter Point 1 for line : ",end="")
    (x0,y0) = (map(int,input().split()))
    print("Enter Point 2 for line : ",end="")
    (x1,y1) = (map(int,input().split()))
    plotLine(x0,y0,x1,y1,win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()

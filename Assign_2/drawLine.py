# We'll have to increase some parameters
# to modularise into separate files
from graphics import *
from transformation import transform

# All cases handled -> all quadrants,negative slopes,
# horizontal lines, vertical lines
def plotLine(x0,y0,x1,y1,window,viewport,win,color):
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
        pt = transform(xp,yp,window,viewport)
        win.plotPixel(pt.getX(),pt.getY(),color)
        if(d<0):
            # Choose East
            d = d + delta_E
        else:
            d = d + delta_NE
            y = y + 1
        x = x + 1

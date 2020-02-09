# Ayush Jain - 2017UCP1168
# Cyrus-Beck/Liang-Barsky Parametric Line Clipping
window = (0,0,0,0)
viewport = (0,0,0,0)
from graphics import *
from drawLine import plotLine

# I am assuming that the line is not degenerate (P0 != P1)
def cyrus_beck_line_clip(x0,y0,x1,y1,x_min,y_min,x_max,y_max):
    tE = 0 ; tL = 1
    if(x0 != x1):
        # Left edge (x = x_min)
        t = (x_min-x0)/(x1-x0)
        sign_check = (x0-x1)
        if(sign_check < 0):
            tE = max(tE,t)
        else:
            tL = min(tL,t)
        # Right edge (x = x_max)
        t = (x0 - x_max)/(x0-x1)
        sign_check = (x1-x0)
        if(sign_check < 0):
            tE = max(tE,t)
        else:
            tL = min(tL,t)
    if(y0 != y1):
        # Bottom edge (y = y_min)
        t = (y_min-y0)/(y1-y0)
        sign_check = (y0-y1)
        if(sign_check < 0):
            tE = max(tE,t)
        else:
            tL = min(tL,t)
        # Top edge
        t = (y0-y_max)/(y0-y1)
        sign_check = (y1-y0)
        if(sign_check < 0):
            tE = max(tE,t)
        else:
            tL = min(tL,t)
    if(tE > tL):
        return None
    else:
        return tuple([tE,tL])

def main():
    global viewport,window
    print("Enter length of viewport : ",end="") ; x = int(input())
    print("Enter width of viewport : ",end="") ; y = int(input())
    # Notation : viewport = (xv_min,yv_min,xv_max,yv_max)
    viewport = (0,0,x,y)
    win = GraphWin("Parametric Line Clipping",x,y)
    win.setBackground(color_rgb(92,219,149))
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
    ###################################################
    print("Enter the coordinates of clipping rectangle")
    print("Enter x_min : ",end=""); x_min = int(input())
    print("Enter y_min : ",end=""); y_min = int(input())
    print("Enter x_max : ",end=""); x_max = int(input())
    print("Enter y_max : ",end=""); y_max = int(input())
    print("Enter point 1 for line(x space y) : ",end="")
    (x0,y0) = (map(int,input().split()))
    print("Enter point 2 for line(x space y) : ",end="")
    (x1,y1) = (map(int,input().split()))
    ###################################################
    plotLine(x_min,y_min,x_min,y_max,window,viewport,win,color_rgb(5,56,107))
    plotLine(x_min,y_min,x_max,y_min,window,viewport,win,color_rgb(5,56,107))
    plotLine(x_min,y_max,x_max,y_max,window,viewport,win,color_rgb(5,56,107))
    plotLine(x_max,y_max,x_max,y_min,window,viewport,win,color_rgb(5,56,107))
    plotLine(x0,y0,x1,y1,window,viewport,win,color_rgb(5,56,107))
    ###################################################
    tt = cyrus_beck_line_clip(x0,y0,x1,y1,x_min,y_min,x_max,y_max)
    if(tt is not None):
        x0_new = int(round(x0 + tt[0]*(x1-x0)))
        y0_new = int(round(y0 + tt[0]*(y1-y0)))
        x1_new = int(round(x0 + tt[1]*(x1-x0)))
        y1_new = int(round(y0 + tt[1]*(y1-y0)))
        plotLine(x0_new,y0_new,x1_new,y1_new,window,viewport,win,"red")
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()

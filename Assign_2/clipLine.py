# Ayush Jain - 2017UCP1168
# Cohen-Sutherland line clipping
window = (0,0,0,0)
viewport = (0,0,0,0)
from graphics import *
from drawLine import plotLine

def cal_outcode(x,y,x_min,y_min,x_max,y_max):
    code = 0
    if(y > y_max):
        code = code | 8
    elif(y < y_min):
        code = code | 4

    if(x > x_max):
        code = code | 2
    elif(x < x_min):
        code = code | 1
    return code

def cohen_Sutherland_clip(x0,y0,x1,y1,x_min,y_min,x_max,y_max,win):
    outcode0 = cal_outcode(x0,y0,x_min,y_min,x_max,y_max)
    outcode1 = cal_outcode(x1,y1,x_min,y_min,x_max,y_max)
    if(x1 != x0):
        slope = (y1-y0)/(x1-x0)
    else:
        slope = None
    done = accept = False
    while(done is False):
        if (outcode0|outcode1) == 0:
            # Trivially Accepted
            done = True ; accept = True
        elif (outcode0 & outcode1) != 0:
            # Trivially Rejected
            done = True
        else:
            if(outcode0):
                tmp_outcode = outcode0
                flag = 0
            else:
                tmp_outcode = outcode1
                flag = 1
            # Find intersections with edges
            if(tmp_outcode & 8):
                if(slope is None):
                    tx = x0
                else:
                    tx = x0 + (y_max-y0)/slope
                ty = y_max
            elif(tmp_outcode & 4):
                if(slope is None):
                    tx = x0
                else:
                    tx = x0 + (y_min-y0)/slope
                ty = y_min
            elif(tmp_outcode & 2):
                tx = x_max
                ty = y0 + (slope)*(x_max-x0)
            else:
                tx = x_min
                ty = y0 + (slope)*(x_min-x0)
            # Now we move outside point to intersection point and update outcode
            if(flag == 0):
                x0 = tx ; y0 = ty
                outcode0 = cal_outcode(x0,y0,x_min,y_min,x_max,y_max)
            else:
                x1 = tx ; y1 = ty
                outcode1 = cal_outcode(x1,y1,x_min,y_min,x_max,y_max)
    if(accept is True):
        x0 = int(round(x0)) ; y0 = int(round(y0))
        x1 = int(round(x1)) ; y1 = int(round(y1))
        plotLine(x0,y0,x1,y1,window,viewport,win,"red")
    return 0

def main():
    global viewport,window
    print("Enter length of viewport : ",end="") ; x = int(input())
    print("Enter width of viewport : ",end="") ; y = int(input())
    # Notation : viewport = (xv_min,yv_min,xv_max,yv_max)
    viewport = (0,0,x,y)
    win = GraphWin("Cohen-Sutherland Line Clipping",x,y)
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
    cohen_Sutherland_clip(x0,y0,x1,y1,x_min,y_min,x_max,y_max,win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()

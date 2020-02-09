# Ayush Jain - 2017UCP1168
# Scan Line Polygon Filling Algorithm
window = (0,0,0,0)
viewport = (0,0,0,0)
from graphics import *
from drawLine import plotLine
from transformation import transform
import math

def polyFill(edges,win):
    for i in range(len(edges)):
        tmp = list(edges[i])
        if(tmp[1] > tmp[3]):
            (tmp[1],tmp[3]) = (tmp[3],tmp[1])
            (tmp[0],tmp[2]) = (tmp[2],tmp[0])
            edges[i] = tuple(tmp)
    y_max = edges[0][3] ; y_min = edges[0][1]
    for i in range(len(edges)):
        if(edges[i][3] > y_max):
            y_max = edges[i][3]
        if(edges[i][1] < y_min):
            y_min = edges[i][1]
    no_of_scan_lines = y_max-y_min+1
    edge_table = list()
    for i in range(no_of_scan_lines):
        edge_table.append([])
    for i in range(len(edges)):
        tmp = edges[i]
        if(tmp[1] != tmp[3]):
            one_by_m = (tmp[2]-tmp[0])/(tmp[3]-tmp[1])
            # y_max, x_of_ymin, 1/m
            tt1 = tuple([tmp[3],tmp[0],one_by_m])
            edge_table[tmp[1]-y_min].append(tt1)
    # Yaha pe sorting na bhi kare toh chalega shayad
    AET = list() ; y = y_min
    while(y <= y_max):
        tmp = edge_table[y-y_min]
        for i in tmp:
            AET.append(i)
        tmp = len(AET) ; i = 0
        while(i<tmp):
            if(AET[i][0] == y):
                del AET[i]
                tmp=len(AET)
            else:
                i=i+1
        AET.sort(key=lambda x:x[1],reverse=False)
        i = 0
        while(i <= len(AET)-2):
            x1 = int(math.ceil(AET[i][1]))    # Round Up
            x2 = int(math.floor(AET[i+1][1])) # Round Down
            for x in range(x1,x2+1):
                pt = transform(xw=x,yw=y,window=window,viewport=viewport)
                win.plotPixel(pt.getX(),pt.getY(),color_rgb(5,56,107))
            i=i+2
        y=y+1
        for i in range(len(AET)):
            tmp = list(AET[i])
            tmp[1] = tmp[1] + tmp[2]
            AET[i] = tuple(tmp)
    return 0


def plotPolygon(vertices,win):
    length = len(vertices) ; i=0
    edges = []
    while(i <= length-2):
        x0 = vertices[i][0] ; y0 = vertices[i][1]
        x1 = vertices[i+1][0] ; y1 = vertices[i+1][1]
        tt1 = tuple([x0,y0,x1,y1])
        plotLine(x0,y0,x1,y1,window,viewport,win,"black")
        edges.append(tt1)
        i += 1
    x0 = vertices[0][0] ; y0 = vertices[0][1]
    x1 = vertices[length-1][0] ; y1 = vertices[length-1][1]
    tt1 = tuple([x0,y0,x1,y1])
    edges.append(tt1)
    plotLine(x0,y0,x1,y1,window,viewport,win,"black")
    polyFill(edges,win)

def main():
    global viewport,window
    print("Enter length of viewport : ",end="") ; x = int(input())
    print("Enter width of viewport : ",end="") ; y = int(input())
    # Notation : viewport = (xv_min,yv_min,xv_max,yv_max)
    viewport = (0,0,x,y)
    win = GraphWin("Scan Line Polygon Filling Algorithm",x,y)
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
    print("Enter number of vertices : ",end="") ; V = int(input()) ;
    print("Enter vertices in clockwise order") ; vertices = []
    for i in range(V):
        print("Enter vertex",i+1,"(x space y) : ",end='')
        tmp = tuple(map(int,input().split()))
        vertices.append(tmp)
    plotPolygon(vertices,win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()

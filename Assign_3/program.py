# 2D Transformations
# Ayush Jain - 2017UCP1168
window = (0,0,0,0)
viewport = (0,0,0,0)
from graphics import *
from drawPolygon import plotPolygon
from drawLine import plotLine
import math

def matrix_multiply(A,B):
    m = len(A) ; n = len(A[0]) ; p = len(B[0])
    res = [[0 for j in range(p)] for i in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                res[i][j] += A[i][k] * B[k][j]
    return res

def translate(tx,ty,A):
    tmp = [ [1,0,tx],
            [0,1,ty],
            [0,0,1] ]
    return matrix_multiply(tmp,A)

def rotate(angle,tt,A):
    angle = angle*(math.pi/180) # Convert to radians
    tmp = translate(-tt[0],-tt[1],A)
    a = math.cos(angle)
    b = math.sin(angle)
    mat = [
        [a, -b , 0],
        [b, a  , 0],
        [0, 0  , 1]
    ]
    tmp = matrix_multiply(mat,tmp)
    tmp = translate(tt[0],tt[1],tmp)
    return (tmp)

def scale(sx,sy,A):
    tmp = [
        [sx, 0 , 0],
        [0 , sy, 0],
        [0,  0 , 1]
    ]
    return matrix_multiply(tmp,A)

def shear(A):
    print("Enter 1 for shear in x or 2 for shear in y : ",end='')
    x = int(input())
    if(x == 1):
        print("Enter shx : ",end='')
        shx = float(input())
        tmp = [
            [1,shx,0],
            [0,1,0],
            [0,0,1]
        ]
    else:
        print("Enter shy : ",end='')
        shy = float(input())
        tmp = [
            [1,0,0],
            [shy,1,0],
            [0,0,1]
        ]
    return matrix_multiply(tmp,A)

def reflect(A,win):
    print("Enter point 1 for line (x space y): ",end='')
    (x0,y0) = (map(int,input().split()))
    print("Enter point 2 for line (x space y): ",end='')
    (x1,y1) = (map(int,input().split()))
    if(x0 != x1):
        slope = (y1-y0)/(x1-x0)
        angle = math.atan(slope)
        angle = angle*(180/math.pi)
    else:
        angle = 90
    plotLine(x0,y0,x1,y1,window,viewport,win,"blue")
    tmp = translate(-x0,-y0,A)
    tmp = rotate(-angle,[0,0],tmp)
    mat = [
        [1,0,0],
        [0,-1,0],
        [0,0,1]
    ]
    tmp = matrix_multiply(mat,tmp)
    tmp = rotate(angle,[0,0],tmp)
    tmp = translate(x0,y0,tmp)
    return tmp

def final(trans,vertices):
    res = []
    for i in range(len(vertices)):
        res.append(matrix_multiply(trans,vertices[i]))
    return res

def main():
    global viewport,window
    print("Enter length of viewport : ",end="") ; x = int(input())
    print("Enter width of viewport : ",end="") ; y = int(input())
    # Notation : viewport = (xv_min,yv_min,xv_max,yv_max)
    viewport = (0,0,x,y)
    win = GraphWin("Transformations",x,y)
    win.setBackground(color_rgb(60, 179, 113))
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
        tmp = list(map(int,input().split()))
        vertices.append([ [tmp[0]],
                          [tmp[1]],
                          [1] ])
    plotPolygon(vertices,window,viewport,win,"black")
    choice = 0
    while(choice != 6):
        tmp = [
            [1,0,0],
            [0,1,0],
            [0,0,1]
        ]
        print()
        print(" 1. Translate")
        print(" 2. Rotate")
        print(" 3. Scale")
        print(" 4. Shear")
        print(" 5. Reflect")
        print(" 6. Exit")
        choice = int(input("Enter choice : "))
        if(choice == 1):
            tx = int(input("Enter tx : "))
            ty = int(input("Enter ty : "))
            tmp = translate(tx,ty,tmp)
        elif(choice == 2):
            (x,y) = (map(int,input("Enter point about which to rotate(x space y) : ").split()))
            angle = int(input("Enter angle in degrees : "))
            tmp = rotate(angle,[x,y],tmp)
        elif(choice == 3):
            sx = float(input("Enter Sx : "))
            sy = float(input("Enter Sy : "))
            tmp = scale(sx,sy,tmp)
        elif(choice == 4):
            tmp = shear(tmp)
        elif(choice == 5):
            tmp = reflect(tmp,win)
        tmp_vertices = final(tmp,vertices)
        plotPolygon(tmp_vertices,window,viewport,win,"red")
        print("Click on viewport to continue")
        win.getMouse()
        plotPolygon(tmp_vertices,window,viewport,win,color_rgb(60, 179, 113))
        plotPolygon(vertices,window,viewport,win,"black")
    win.close()

if __name__ == '__main__':
    main()

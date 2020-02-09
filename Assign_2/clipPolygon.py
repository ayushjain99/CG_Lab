# Ayush Jain - 2017UCP1168
# Sutherland Hodgman Polygon Clipping Algorithm
# Vertical Lines, Equal slopes(m1=m2) for intersection not taken care of
window = (0,0,0,0)
viewport = (0,0,0,0)
from graphics import *
from drawLine import plotLine

def sutherland_Hodgman(vertices,vertices_c):
    for i in range(len(vertices_c)):
        x1 = vertices_c[i][0] ; y1 = vertices_c[i][1]
        x2 = vertices_c[(i+1)%len(vertices_c)][0] ; y2 = vertices_c[(i+1)%len(vertices_c)][1]
        tmp = list()
        for j in range(len(vertices)):
            x3 = vertices[j][0] ; y3 = vertices[j][1]
            x4 = vertices[(j+1)%len(vertices)][0] ; y4 = vertices[(j+1)%len(vertices)][1]
            P1 = (y3-y1)*(x2-x1) - (y2-y1)*(x3-x1)
            P2 = (y4-y1)*(x2-x1) - (y2-y1)*(x4-x1)
            if(P1 < 0):
                I1 = "in"
            else:
                I1 = "out"
            if(P2 < 0):
                I2 = "in"
            else:
                I2 = "out"
            if(I1 == "in") and (I2 == "in"):
                tmp.append([x4,y4])
            elif(I1 == "in") and (I2 == "out"):
                # Find pt of intersection
                m1 = (y2-y1)/(x2-x1)
                m2 = (y4-y3)/(x4-x3)
                c1 = y1 - (m1*x1)
                c2 = y3 - (m2*x3)
                x_int = (c2-c1)/(m1-m2)
                y_int = (m1*x_int) + (c1)
                tmp.append([x_int,y_int])
            elif(I1=="out") and (I2=="in"):
                m1 = (y2-y1)/(x2-x1)
                m2 = (y4-y3)/(x4-x3)
                c1 = y1 - (m1*x1)
                c2 = y3 - (m2*x3)
                x_int = (c2-c1)/(m1-m2)
                y_int = (m1*x_int) + (c1)
                tmp.append([x_int,y_int])
                tmp.append([x4,y4])
        vertices = tmp
    return vertices


def main():
    global viewport,window
    print("Enter length of viewport : ",end="") ; x = int(input())
    print("Enter width of viewport : ",end="") ; y = int(input())
    # Notation : viewport = (xv_min,yv_min,xv_max,yv_max)
    viewport = (0,0,x,y)
    win = GraphWin("Sutherland Hodgman Polygon Clipping",x,y)
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
    print("Enter coordinates of polygon to be clipped in clockwise order")
    print("Number of vertices : ",end="")
    V = int(input())
    vertices = []
    for i in range(V):
        print("Enter V",i+1,"(x space y) : ",end="")
        (x,y) = (map(int,input().split()))
        vertices.append([x,y])
    for i in range(V-1):
        x1 = vertices[i][0] ; y1 = vertices[i][1]
        x2 = vertices[i+1][0] ; y2 = vertices[i+1][1]
        plotLine(x1,y1,x2,y2,window,viewport,win,color_rgb(5,56,107))
    x1 = vertices[V-1][0] ; y1 = vertices[V-1][1]
    x2 = vertices[0][0] ; y2 = vertices[0][1]
    plotLine(x1,y1,x2,y2,window,viewport,win,color_rgb(5,56,107))
    ###################################################
    print("Enter coordinates of clipping polygon(convex)in clockwise order")
    print("Number of vertices : ",end="")
    VC = int(input())
    vertices_c = []
    for i in range(VC):
        print("Enter V",i+1,"(x space y) : ",end="")
        (x,y) = (map(int,input().split()))
        vertices_c.append([x,y])
    for i in range(VC-1):
        x1 = vertices_c[i][0] ; y1 = vertices_c[i][1]
        x2 = vertices_c[i+1][0] ; y2 = vertices_c[i+1][1]
        plotLine(x1,y1,x2,y2,window,viewport,win,"black")
    x1 = vertices_c[VC-1][0] ; y1 = vertices_c[VC-1][1]
    x2 = vertices_c[0][0] ; y2 = vertices_c[0][1]
    plotLine(x1,y1,x2,y2,window,viewport,win,"black")
    ##################################################
    new_vertices = sutherland_Hodgman(vertices,vertices_c)
    V = len(new_vertices)
    for i in range(V-1):
        x1 = new_vertices[i][0] ; y1 = new_vertices[i][1]
        x2 = new_vertices[i+1][0] ; y2 = new_vertices[i+1][1]
        plotLine(x1,y1,x2,y2,window,viewport,win,"red")
    x1 = new_vertices[V-1][0] ; y1 = new_vertices[V-1][1]
    x2 = new_vertices[0][0] ; y2 = new_vertices[0][1]
    plotLine(x1,y1,x2,y2,window,viewport,win,"red")
    ##################################################
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()

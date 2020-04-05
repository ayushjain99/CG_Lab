# Projections
# Ayush Jain - 2017UCP1168
window = (0,0,0,0)
viewport = (0,0,0,0)
from graphics import *
from drawLine import plotLine
import math

def matrix_multiply(A,B):
    m = len(A)
    if(type(A[0]) is type(1)) or (type(A[0]) is type(1.5)):
        tmp = []
        for i in range(4):
            x = (A[0]*B[0][i]) + (A[1]*B[1][i]) + (A[2]*B[2][i]) + (A[3]*B[3][i])
            tmp.append(x)
        return tmp
    else:
        n = len(A[0])
    p = len(B[0])
    res = [[0 for j in range(p)] for i in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                res[i][j] += A[i][k] * B[k][j]
    return res

def project_matrix(ref_point,normal,dop):
    (x0,y0,z0) = ref_point
    (n1,n2,n3) = normal
    (a,b,c) = dop
    d0 = (x0*n1) + (y0*n2) + (z0*n3)
    d1 = (a*n1) + (b*n2) + (c*n3)
    mat = [
        [d1-(a*n1) , -b*n1 , -c*n1 , 0],
        [-a*n2 , d1-(b*n2) , -c*n2 , 0],
        [-a*n3 , -b*n3 , d1-(c*n3) , 0],
        [a*d0 , b*d0 , c*d0 , d1]
    ]
    return mat

def project_matrix_perspective(ref_point,normal,cop):
    (x0,y0,z0) = ref_point
    (n1,n2,n3) = normal
    (a,b,c) = cop
    d0 = (x0*n1) + (y0*n2) + (z0*n3)
    d1 = (a*n1) + (b*n2) + (c*n3)
    alpha = d0 - d1
    mat = [
        [alpha+(n1*a) , n1*b , n1*c , n1],
        [n2*a , alpha+(n2*b) , n2*c , n2],
        [n3*a , n3*b , alpha+(n3*c) , n3],
        [-a*d0 , -b*d0 , -c*d0 , -d1]
    ]
    return mat

def make_viewplane_xy(ref_point,normal):
    # We transform the viewplane to xy plane by one translation and two rotations
    # So as to display the viewplane on screen
    (x0,y0,z0) = ref_point
    (n1,n2,n3) = normal
    T1 = [
        [1,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [-x0,-y0,-z0,1]
    ]
    l1 = math.sqrt((n1*n1) + (n3*n3))
    cos_alpha = n3/l1
    sin_alpha = -(n1/l1)
    T2 = [
        [cos_alpha,0,-sin_alpha,0],
        [0,1,0,0],
        [sin_alpha,0,cos_alpha,0],
        [0,0,0,1]
    ]

    T1 = matrix_multiply(T1,T2)
    D = math.sqrt( (l1*l1) + (n2*n2) )
    cos_phi = l1/D
    sin_phi = n2/D
    T2 = [
        [1,0,0,0],
        [0,cos_phi,sin_phi,0],
        [0,-sin_phi,cos_phi,0],
        [0,0,0,1]
    ]
    T1 = matrix_multiply(T1,T2)
    return T1

def main():
    global viewport,window
    print("Enter length of viewport : ",end="") ; x = int(input())
    print("Enter width of viewport : ",end="") ; y = int(input())
    # Notation : viewport = (xv_min,yv_min,xv_max,yv_max)
    viewport = (0,0,x,y)
    win = GraphWin("Projections",x,y)
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
    # CUBE(SIDE = 300) - 12 Edges, Homogeneous Coordinates
    points = [
        [ [0,300,300,1] , [0,300,0,1] ],
        [ [0,300,0,1] , [300,300,0,1] ],
        [ [300,300,0,1] , [300,300,300,1] ],
        [ [300,300,300,1] , [0,300,300,1] ],
        [ [0,0,300,1] , [0,0,0,1] ],
        [ [0,0,0,1] , [300,0,0,1] ],
        [ [300,0,0,1] , [300,0,300,1] ],
        [ [300,0,300,1] , [0,0,300,1] ],
        [ [0,0,300,1] , [0,300,300,1] ],
        [ [0,0,0,1] , [0,300,0,1] ],
        [ [300,0,300,1] , [300,300,300,1] ],
        [ [300,0,0,1] , [300,300,0,1] ]
    ]
    print(" 1. Orthographic - Top View")
    print(" 2. Orthographic - Front View")
    print(" 3. Orthographic - Side View")
    print(" 4. Orthographic - Isometric")
    print(" 5. Oblique - General Parallel")
    print(" 6. General Perspective")
    choice = int(input(" Enter choice : "))
    if(choice == 1):
        p_mat = [
            [1,0,0,0],
            [0,0,0,0],
            [0,0,1,0],
            [0,0,0,1]
        ]
        ref_point = (0,0,0)
        normal = dop = (0,1,0)
    elif(choice == 2):
        p_mat = [
            [1,0,0,0],
            [0,1,0,0],
            [0,0,0,0],
            [0,0,0,1]
        ]
        ref_point = (0,0,0)
        normal = dop = (0,0,1)
    elif(choice == 3):
        p_mat = [
            [0,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1]
        ]
        ref_point = (0,0,0)
        normal = dop = (1,0,0)
    elif(choice == 4):
        print("Enter reference point of PP(x space y space z) : ",end='')
        ref_point = tuple(map(int,input().split()))
        normal = dop = (1,1,1)
        p_mat = project_matrix(ref_point,normal,dop)
    elif(choice == 5):
        print("Enter reference point of PP(x space y space z) : ",end='')
        ref_point = tuple(map(int,input().split()))
        print("Enter normal to the plane(n1 space n2 space n3) : ",end="")
        normal = tuple(map(int,input().split()))
        print("Enter the Direction of Projection(a space b space c) : ",end="")
        dop = tuple(map(int,input().split()))
        p_mat = project_matrix(ref_point,normal,dop)
    elif(choice == 6):
        print("Enter reference point of PP(x space y space z) : ",end='')
        ref_point = tuple(map(int,input().split()))
        print("Enter normal to the plane(n1 space n2 space n3) : ",end="")
        normal = tuple(map(int,input().split()))
        print("Enter the COP(x space y space z) : ",end="")
        cop = tuple(map(int,input().split()))
        p_mat = project_matrix_perspective(ref_point,normal,cop)

    q_mat = make_viewplane_xy(ref_point,normal)
    for i in range(12):
        point1 = points[i][0]
        point2 = points[i][1]
        point1 = matrix_multiply(point1,p_mat)
        point2 = matrix_multiply(point2,p_mat)
        # Homogenize the points again
        if(point1[3] != 1):
            point1[0] = point1[0]/point1[3]
            point1[1] = point1[1]/point1[3]
            point1[2] = point1[2]/point1[3]
            point1[3] = 1
        if(point2[3] != 1):
            point2[0] = point2[0]/point2[3]
            point2[1] = point2[1]/point2[3]
            point2[2] = point2[2]/point2[3]
            point2[3] = 1
        point1 = matrix_multiply(point1,q_mat)
        point2 = matrix_multiply(point2,q_mat)
        points[i][0] = point1
        points[i][1] = point2

    for i in range(12):
        point1 = points[i][0]
        point2 = points[i][1]
        x0 = point1[0] ; y0 = point1[1]
        x1 = point2[0] ; y1 = point2[1]
        plotLine(x0,y0,x1,y1,window,viewport,win,"black")

    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()

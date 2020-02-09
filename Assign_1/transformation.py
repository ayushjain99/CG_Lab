from graphics import *
window = (0,0,0,0)
viewport = (0,0,0,0)

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

def main():
    global viewport,window
    win = GraphWin("Window to Viewport Transformation",500,500)
    # win.setBackground(color_rgb(60, 179, 113))
    win.setCoords(0,0,100,100)
    # Notation : viewport = (xv_min,yv_min,xv_max,yv_max)
    viewport = (0,0,500,500)
    # Notation : window = (xw_min,yw_min,xw_max,yw_max)
    window = (-100,-100,100,100)
    pt = transform(0,0)
    print(pt.getX(),pt.getY())
    win.plotPixel(pt.getX(),pt.getY(),"red")
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()

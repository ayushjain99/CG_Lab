from drawLine import plotLine

def plotPolygon(vertices,window,viewport,win,color):
    length = len(vertices) ; i=0
    while(i <= length-2):
        x0 = vertices[i][0][0] ; y0 = vertices[i][1][0]
        x1 = vertices[i+1][0][0] ; y1 = vertices[i+1][1][0]
        plotLine(x0,y0,x1,y1,window,viewport,win,color)
        i += 1
    x0 = vertices[0][0][0] ; y0 = vertices[0][1][0]
    x1 = vertices[length-1][0][0] ; y1 = vertices[length-1][1][0]
    plotLine(x0,y0,x1,y1,window,viewport,win,color)

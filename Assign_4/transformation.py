# Just the transform method
# Trying to modularise little bit
from graphics import *

def transform(xw,yw,window,viewport):
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

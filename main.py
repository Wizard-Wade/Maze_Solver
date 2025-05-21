from Window import *
from Point import *
from Line import *

win = Window(800, 600)
l = line(point(50, 50), point(400, 400))
win.draw_line(l, "black")
win.wait_for_close()
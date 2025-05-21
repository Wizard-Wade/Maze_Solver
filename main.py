from Window import *
from Point import *
from Line import *
from Cell import *

win = window(800, 600)
c = cell(win)
c.draw(point(50, 50), point(400, 400))
win.wait_for_close()
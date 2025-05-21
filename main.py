from Window import *
from Point import *
from Line import *
from Cell import *

win = window(800, 600)
c = cell(win)
c2 = cell(win)
c.draw(point(50, 50), point(100, 100))
c2.draw(point(100, 50), point(150, 100))
c.draw_move(c2)

win.wait_for_close()
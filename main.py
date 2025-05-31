from Window import *
from Point import *
from Line import *
from Cell import *
from maze import maze

win = window(802, 602)
m1 = maze(2,2,0,0,25,25,win)
m1.solve()

win.wait_for_close()
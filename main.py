from Window import *
from Point import *
from Line import *
from Cell import *
from maze import maze

win = window(802, 602)
maze(2,2,0,0,50,50,win, 10)

win.wait_for_close()
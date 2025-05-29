from Window import *
from Point import *
from Line import *
from Cell import *
from maze import maze

win = window(800, 600)
maze(2,2,0,0,50,50,win)

win.wait_for_close()
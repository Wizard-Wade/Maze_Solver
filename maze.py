from Cell import *
from Point import point
import time
import tkinter

class maze:
    def __init__(
            self,
            x1 = 0,
            y1 = 0,
            num_rows = 0,
            num_cols = 0,
            cell_size_x = 0,
            cell_size_y = 0,
            win: window = None,
        ):
        self.__x1 = x1    
        self.__y1 = y1
        
        if win !=None and num_cols is 0:
            self.__num_cols = int((win.width - self.__x1) / cell_size_x)
            self.__num_rows = int((win.height - self.__y1) / cell_size_y)
        else:
            self.__num_rows = num_rows
            self.__num_cols = num_cols
            
        if win != None and cell_size_x is 0:
            self.__cell_size_x = int((win.width - self.__x1) / num_cols)
            self.__cell_size_y = int((win.height - self.__y1) / num_rows)
        else:
            self.__cell_size_x = cell_size_x
            self.__cell_size_y = cell_size_y
        
        self.__win = win
        self.__cells = [None] * self.__num_cols
        self.__create_cells()
        self.__break_entrance_and_exit()
        
    def __create_cells(self):
        for c in range(self.__num_cols):
            self.__cells[c] = []
            for r in range(self.__num_rows):
                self.__cells[c].append(cell(self.__win))
                self.__draw_cell(c,r)
                
    def __draw_cell(self, i, j):
        x = i*self.__cell_size_x + self.__x1
        y = j*self.__cell_size_y + self.__y1
        c:cell = self.__cells[i][j]
        c.draw(point(x, y), point(x+self.__cell_size_x, y+self.__cell_size_y))
        self.__animate()
    
    def __animate(self):
        if self.__win == None: return
        self.__win.redraw()
        time.sleep(0.01)
        
    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0,0)
        c = self.__cells[self.__num_cols-1][self.__num_rows-1]
        c.has_bottom_wall = False
        self.__draw_cell(self.__num_cols-1, self.__num_rows-1)
        
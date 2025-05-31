from Cell import *
from Point import point
import time
import random

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
            seed = None
        ):
        self.__x1 = x1    
        self.__y1 = y1
        
        if win !=None and num_cols == 0:
            self.__num_cols = int((win.width - self.__x1) / cell_size_x)
            self.__num_rows = int((win.height - self.__y1) / cell_size_y)
        else:
            self.__num_rows = num_rows
            self.__num_cols = num_cols
            
        if win != None and cell_size_x == 0:
            self.__cell_size_x = int((win.width - self.__x1) / num_cols)
            self.__cell_size_y = int((win.height - self.__y1) / num_rows)
        else:
            self.__cell_size_x = cell_size_x
            self.__cell_size_y = cell_size_y
            
        if seed is not None:
            random.seed(seed)
        
        self.__win = win
        self.__cells = [None] * self.__num_cols
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)
        self.__reset_cells_visited()
        
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
        time.sleep(0.0001)
        
    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0,0)
        c = self.__cells[self.__num_cols-1][self.__num_rows-1]
        c.has_bottom_wall = False
        self.__draw_cell(self.__num_cols-1, self.__num_rows-1)
        
    def __break_walls_r(self, i, j):
        c:cell = self.__cells[i][j]
        c.visited = True
        while True:
            to_visit = []
            if i != 0 and not self.__cells[i-1][j].visited:
                to_visit.append(("l", i-1, j))
            if i != self.__num_cols-1 and not self.__cells[i+1][j].visited:
                to_visit.append(("r", i+1, j))
            if j != 0 and not self.__cells[i][j-1].visited:
                to_visit.append(("u", i, j-1))
            if j != self.__num_rows-1 and not self.__cells[i][j+1].visited:
                to_visit.append(("d", i, j+1))
            
            if not to_visit:
                self.__draw_cell(i,j)
                return            
            direction = to_visit[random.randrange(0, len(to_visit))]
            ni = direction[1]
            nj = direction[2]
            match direction[0]:
                case "l":
                    c.has_left_wall = False
                    self.__cells[ni][nj].has_right_wall = False
                case "r":
                    c.has_right_wall = False
                    self.__cells[ni][nj].has_left_wall = False
                case "u":
                    c.has_top_wall = False
                    self.__cells[ni][nj].has_bottom_wall = False
                case "d":
                    c.has_bottom_wall = False
                    self.__cells[ni][nj].has_top_wall = False
            self.__break_walls_r(ni,nj)
        
    def __reset_cells_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__cells[i][j].visited = False
    
    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self, i, j):
        self.__animate()
        current_cell: cell = self.__cells[i][j]
        current_cell.visited = True
        if i == self.__num_cols-1 and j == self.__num_rows-1:
            return True
        
        walls = current_cell.get_walls()
        for (idx, wall) in enumerate(walls):
            if wall or idx ==0 and i == 0 and j == 0:
                continue
            
            next = self._get_next_available_cell(idx, i, j)
            i1 = next[0]
            j1 = next[1]
            
            next_cell: cell  = self.__cells[i1][j1]
            if next_cell.visited:
                continue
            
            current_cell.draw_move(next_cell)
            if self._solve_r(i1, j1):
                return True
            current_cell.draw_move(next_cell, True)
            
        return False
    
    def _get_next_available_cell(self, idx, i, j):
        if idx == 0:
            #open to cell above
            i1 = i
            j1 = j-1
        elif idx == 1:
            #open to cell left
            i1 = i-1
            j1 = j
        elif idx == 2:
            #open to cell below
            i1 = i
            j1 = j+1
        elif idx == 3:
            #open to cell right
            i1 = i+1
            j1 = j
        else:
            # somehow ended up in a cell with all walls
            raise Exception("Cell has no path out")
        
        return i1, j1
from Line import line
from Point import point
from Window import window

class cell:
    def __init__(self, win: window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = win
        self.visited = False
    
    def draw(self, point1: point, point2: point, fillcolor: str = "black"):
        self.__x1 = point1.x
        self.__y1 = point1.y
        self.__x2 = point2.x
        self.__y2 = point2.y
        if self.__win == None: return
        
        erasecolor = "white"
        if not self.has_left_wall:
            self.__win.draw_line(line(point(self.__x1, self.__y1), point(self.__x1, self.__y2)), erasecolor)
        else:
            self.__win.draw_line(line(point(self.__x1, self.__y1), point(self.__x1, self.__y2)), fillcolor)
            
        if self.has_bottom_wall:
            self.__win.draw_line(line(point(self.__x1, self.__y2), point(self.__x2, self.__y2)), fillcolor)
        else:
            self.__win.draw_line(line(point(self.__x1, self.__y2), point(self.__x2, self.__y2)), erasecolor)
            
        if self.has_right_wall:
            self.__win.draw_line(line(point(self.__x2, self.__y1), point(self.__x2, self.__y2)), fillcolor)
        else:
            self.__win.draw_line(line(point(self.__x2, self.__y1), point(self.__x2, self.__y2)), erasecolor)
            
        if self.has_top_wall:
            self.__win.draw_line(line(point(self.__x1, self.__y1), point(self.__x2, self.__y1)), fillcolor)
        else:
            self.__win.draw_line(line(point(self.__x1, self.__y1), point(self.__x2, self.__y1)), erasecolor)      
    
    def centroid(self):
        return point((self.__x2 - self.__x1)/2 + self.__x1, (self.__y2 - self.__y1)/2 + self.__y1)
    
    def draw_move(self, to_cell, undo=False):
        start_pt = self.centroid()
        end_pt = to_cell.centroid()
        if self.__win == None: return
        self.__win.draw_line(line(start_pt, end_pt), "white" if undo else "red")
    
    def get_walls(self):
        return [self.has_top_wall, self.has_left_wall, self.has_bottom_wall,self.has_right_wall]
        

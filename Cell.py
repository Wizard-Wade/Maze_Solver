from Line import line
from Point import point
from Window import window

class cell:
    def __init__(self, win: window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = win
    
    def draw(self, point1: point, point2: point, fillcolor: str = "black"):
        self.__x1 = point1.x
        self.__y1 = point1.y
        self.__x2 = point2.x
        self.__y2 = point2.y
        if self.has_left_wall:
            self.__win.draw_line(line(point(self.__x1, self.__y1), point(self.__x1, self.__y2)), fillcolor)
        if self.has_bottom_wall:
            self.__win.draw_line(line(point(self.__x1, self.__y1), point(self.__x2, self.__y1)), fillcolor)
        if self.has_right_wall:
            self.__win.draw_line(line(point(self.__x2, self.__y1), point(self.__x2, self.__y2)), fillcolor)
        if self.has_top_wall:
            self.__win.draw_line(line(point(self.__x1, self.__y2), point(self.__x2, self.__y2)), fillcolor)
    
    def centroid(self):
        return point((self.__x2 - self.__x1)/2 + self.__x1, (self.__y2 - self.__y1)/2 + self.__y1)
    
    def draw_move(self, to_cell, undo=False):
        start_pt = self.centroid()
        end_pt = to_cell.centroid()
        self.__win.draw_line(line(start_pt, end_pt), "black" if undo else "grey")
        
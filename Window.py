from tkinter import Tk, BOTH, Canvas
from Line import line

class window:
    def __init__(self, width, height):
        self._tk_root = Tk()
        self._tk_root.title = "Maze Solver"
        self._canvas = Canvas(self._tk_root, bg = "white", height=height, width=width)
        self._canvas.pack()
        self._run_state = False
        self._tk_root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self):
        self._tk_root.update_idletasks()
        self._tk_root.update()
        
    def wait_for_close(self):
        self._run_state = True
        while self._run_state:
            self.redraw()
        print("Window closed")
            
    def close(self):
        self._run_state = False
        
    
    def draw_line(self, line: line, fill_color: str):
        line.draw(self._canvas, fill_color)
        

        

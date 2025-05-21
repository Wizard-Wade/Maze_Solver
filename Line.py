from tkinter import Canvas
from Point import point

class line:
    def __init__(self, start_point: point, end_point: point):
        self.startpoint = start_point
        self.endpoint = end_point
    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(self.startpoint.x, self.startpoint.y, self.endpoint.x, self.endpoint.y, fill= fill_color, width=2)
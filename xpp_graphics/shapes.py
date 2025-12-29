import pyglet
from pyglet import shapes
from math import atan2, degrees, sqrt

class Rectangle:
    def __init__(self, x, y, width, height, color=(255,0,0), batch=None):
        self.rect = shapes.Rectangle(x, y, width, height, color=color, batch=batch)

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        self.rect.draw()

class Circle:
    def __init__(self, x, y, radius, color=(0,255,0), batch=None):
        self.circle = shapes.Circle(x, y, radius, color=color, batch=batch)

    def set_position(self, x, y):
        self.circle.x = x
        self.circle.y = y

    def draw(self):
        self.circle.draw()

class Line:
    def __init__(self, x1, y1, x2, y2, color=(0,0,255), batch=None):
        self.line = shapes.Line(x1, y1, x2, y2, color=color, batch=batch)

    def draw(self):
        self.line.draw()

# Optional thick line for custom width
class ThickLine:
    def __init__(self, x1, y1, x2, y2, width=3, color=(0,0,255), batch=None):
        dx = x2 - x1
        dy = y2 - y1
        length = sqrt(dx*dx + dy*dy)
        angle = degrees(atan2(dy, dx))
        self.rect = shapes.Rectangle(x1, y1, length, width, color=color, batch=batch)
        self.rect.rotation = angle

    def draw(self):
        self.rect.draw()

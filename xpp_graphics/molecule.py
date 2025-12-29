import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from xpp_graphics.shapes import Circle

class Molecule(Circle):
    def __init__(self, x, y, radius=10, color=(0,255,0), vx=100, vy=80):
        super().__init__(x, y, radius, color)
        self.vx = vx  # velocity x (pixels/sec)
        self.vy = vy  # velocity y

    def update(self, dt):
        # Move molecule
        self.circle.x += self.vx * dt
        self.circle.y += self.vy * dt

        # Bounce off walls (assuming 800x600 window)
        if self.circle.x - self.circle.radius < 0 or self.circle.x + self.circle.radius > 800:
            self.vx *= -1
        if self.circle.y - self.circle.radius < 0 or self.circle.y + self.circle.radius > 600:
            self.vy *= -1

# xpp_graphics/dna.py
from xpp_graphics.shapes import Circle

class Nucleotide:
    def __init__(self, x, y, radius=5, color=(0,255,0)):
        self.circle = Circle(x, y, radius, color=color)
        self.vx = 0
        self.vy = 0

    def update(self, dt):
        self.circle.x += self.vx * dt
        self.circle.y += self.vy * dt

    def draw(self):
        self.circle.draw()


class DNAChain:
    def __init__(self, start_x, start_y, length=20, spacing=15):
        self.nucleotides = []
        for i in range(length):
            self.nucleotides.append(Nucleotide(start_x + i*spacing, start_y))

    def update(self, dt):
        k = 50  # spring constant
        damping = 0.98
        for i in range(len(self.nucleotides)-1):
            a = self.nucleotides[i]
            b = self.nucleotides[i+1]
            dx = b.circle.x - a.circle.x
            dy = b.circle.y - a.circle.y
            dist = (dx**2 + dy**2)**0.5
            if dist == 0: continue
            force = k * (dist - 15)
            fx = force * dx / dist
            fy = force * dy / dist
            a.vx += fx * dt
            a.vy += fy * dt
            b.vx -= fx * dt
            b.vy -= fy * dt

        for n in self.nucleotides:
            n.vx *= damping
            n.vy *= damping
            n.update(dt)

    def draw(self):
        for n in self.nucleotides:
            n.draw()

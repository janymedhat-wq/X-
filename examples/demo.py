import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from xpp_graphics.window import Window
from xpp_graphics.renderer import Renderer
from xpp_graphics.scene import Scene
from xpp_graphics.molecule import Molecule
import pyglet
import random

# Window & renderer
win = Window(800, 600, "X++ API Molecular Simulation")
renderer = Renderer(win)

# Scene
scene = Scene()

# Add molecules
for _ in range(20):
    mol = Molecule(
        x=random.randint(50,750),
        y=random.randint(50,550),
        radius=10,
        color=(random.randint(50,255), random.randint(50,255), random.randint(50,255)),
        vx=random.randint(-200,200),
        vy=random.randint(-200,200)
    )
    scene.add(mol)

# Update loop
def update(dt):
    scene.update(dt)

pyglet.clock.schedule_interval(update, 1/60)  # 60 FPS

# Draw callback
@win.window.event
def on_draw():
    renderer.clear()
    scene.draw()

pyglet.app.run()

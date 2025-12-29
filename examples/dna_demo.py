import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from xpp_graphics.window import Window
from xpp_graphics.renderer import Renderer
from xpp_graphics.scene import Scene
from xpp_graphics.dna import DNAChain
import pyglet

# Window & scene
win = Window(800, 600, "DNA Simulation Demo")
renderer = Renderer(win)
scene = Scene()

# Create DNA chain
dna = DNAChain(100, 300, length=30)
scene.add(dna)

# Update loop
def update(dt):
    scene.update(dt)

pyglet.clock.schedule_interval(update, 1/60)

# Draw callback
@win.window.event
def on_draw():
    renderer.clear()
    scene.draw()

pyglet.app.run()

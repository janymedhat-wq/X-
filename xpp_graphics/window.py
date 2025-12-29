import pyglet

class Window:
    def __init__(self, width=800, height=600, title="X++ Graphics"):
        self.window = pyglet.window.Window(width, height, title)
        self.draw_callbacks = []
        self.is_open_flag = True
        self.window.push_handlers(on_close=self.on_close)

    def on_close(self):
        self.is_open_flag = False

    def register_draw(self, func):
        """Register a function to draw each frame"""
        self.draw_callbacks.append(func)
        self.window.push_handlers(self)

    def draw(self):
        for func in self.draw_callbacks:
            try:
                func()
            except Exception as e:   # ✅ Python 3 syntax
                print("Error during draw callback:", e)

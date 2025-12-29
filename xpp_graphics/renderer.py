class Renderer:
    def __init__(self, window):
        self.window = window

    def clear(self):
        self.window.window.clear()

    def present(self):
        pass  # Pyglet automatically flips the window

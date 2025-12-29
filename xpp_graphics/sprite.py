import pyglet

class Sprite:
    def __init__(self, image_file):
        try:
            self.sprite = pyglet.sprite.Sprite(pyglet.image.load(image_file))
        except Exception as e:
            print(f"Failed to load image '{image_file}':", e)
            raise

    def set_position(self, x, y):
        self.sprite.x = x
        self.sprite.y = y

    def draw(self):
        try:
            self.sprite.draw()
        except Exception as e:
            print("Failed to draw sprite:", e)

class Scene:
    def __init__(self):
        """Initialize an empty scene"""
        self.objects = []

    def add(self, obj):
        """Add a drawable object (sprite, shape, molecule, etc.)"""
        if obj not in self.objects:
            self.objects.append(obj)

    def remove(self, obj):
        """Remove an object if it exists in the scene"""
        if obj in self.objects:
            self.objects.remove(obj)

    def update(self, dt):
        """
        Update all objects in the scene.
        If an object has an 'update(dt)' method, it will be called.
        This allows simulation of movement, physics, etc.
        """
        for obj in self.objects:
            try:
                if hasattr(obj, "update"):
                    obj.update(dt)
            except Exception as e:
                print("Error updating object:", e)

    def draw(self):
        """Draw all objects in the scene safely"""
        for obj in self.objects:
            try:
                obj.draw()
            except Exception as e:
                print("Error drawing object:", e)

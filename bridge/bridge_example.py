from abc import ABC 

 
class Render(ABC):
    def render_circle(self, radius):
        pass


class VectorRenderer(Render):
    def render_circle(self, radius):
        print(f"VectorRenderer(Render) {radius}")

        
class RasterRenderer(Render):
    def render_circle(self, radius):
        print(f"RasterRenderer(Render) {radius}")


class Shape:
    def __init__(self,renderer):
        self.renderer = renderer

    def draw(self): pass
    def resize(self, factor): pass


class Circle(Shape):
    def __init__(self, rendered, radius):
        super().__init__(rendered)
        self.radius = radius

    def draw(self): 
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == "__main__":
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle1 = Circle(raster, 6)
    circle1.draw()
    circle1.resize(2)
    circle1.draw()
    circle2 = Circle(vector, 22)
    circle2.draw()
    circle2.resize(2)
    circle2.draw()
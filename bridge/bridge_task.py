import sys
from abc import ABC 

# class Shape:
#     def __init__(self):
#         self.name = None
#
#
# class Triangle(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Triangle'
#
#
# class Square(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Square'
#
#
# class VectorSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as lines'
#
#
# class RasterSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as pixels'

# imagine VectorTriangle and RasterTriangle are here too

class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None


class Shape:
    def __init__(self, renderer, name):
        self.renderer = renderer
        self.name = name

    def __str__(self) -> str:
        return f'Drawing {self.name} as {self.renderer.what_to_render_as}'


class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer, 'Square')


class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer, 'Triangle')


class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return "lines"


class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return "pixels"


#код ниже руками не трогать
sq = Square(VectorRenderer())
tr = Triangle(RasterRenderer())

print(f'{str(sq)} {str(tr)}')
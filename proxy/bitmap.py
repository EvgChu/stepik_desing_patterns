class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        print(f"Loading image from {self.filename}")

    def draw(self):
        print(f"Drawing image {self.filename}")

class LazyBitmap: 
    """ Virtual proxy"""
    def __init__(self, filename):
        self.filename = filename
        self._bitmap = None

    def draw(self):
        if not self._bitmap:
            self._bitmap = Bitmap(self.filename)
        self._bitmap.draw()

def draw_image(image):
    print(f"About to draw image")
    image.draw()
    print(f"Done drawing image")

if __name__ == "__main__":
    bmp = LazyBitmap('fake.img')
    draw_image(bmp)
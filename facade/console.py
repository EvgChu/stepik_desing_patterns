

class Buffer:
    def __init__(self, width=30, height=30) -> None:
        self.width = width
        self.height = height
        self.buffer = [' '] * (width * height)

    def __getitem__(self, item):
        return self.buffer.__getitem__(item)

    def write(self, text):
        self.buffer += text


class Viewport:
    def __init__(self, buffer=Buffer()) -> None:
        self.buffer = buffer
        self.offset = 0

    def get_char_at(self, index):
        return self.buffer[index + self.offset]

    def append(self, text):
       self.buffer.write(text)

class Console:
    def __init__(self, buffer=Buffer()) -> None:
        b = Buffer()
        self.current_viewport = Viewport(b)
        self.buffers = [b]
        self.viewports = [self.current_viewport]

    def get_char_at(self, index):
        return self.current_viewport.get_char_at(index)

    def write(self, text):
        self.current_viewport.buffer.write(text)

if __name__ == "__main__":
    c = Console()
    c.write('hello')
    ch = c.get_char_at(0)
    print(ch)
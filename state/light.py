from abc import ABC


class Swith:
    def __init__(self) -> None:
        self.state = OffState()
    
    def on(self):
        self.state.on(self)

    def off(self):
        self.state.off(self)


class State(ABC):
    def on(self, swith):
        print('Light is already on')

    def off(self, swith):
        print('Light is already off')


class OnState(State):
    def __init__(self) -> None:
        print('Light turned on')
        
    def on(self, switch):
        print('Turning light off...')
        switch.state = OffState()


class OffState(State):
    def __init__(self) -> None:
        print('Light turned off')

    def on(self, switch):
        print('Turning light on...')
        switch.state = OnState()


if __name__ == "__main__":
    sw = Swith()
    sw.on()
    sw.off()
    sw.off()

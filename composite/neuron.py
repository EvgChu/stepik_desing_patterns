
from abc import ABC
from collections.abc import Iterable


class Connectable(Iterable, ABC):
    def connect_to(self, other):
        if self == other:
            return
        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)

class Neuron(Connectable):
    def __init__(self, name: str) -> None:
        self.name = name
        self.inputs = [] 
        self.outputs = [] 

    def __str__(self) -> str:
        return f'{self.name}, ' \
            f'{len(self.inputs)} inputs,' \
            f'{len(self.outputs)} outputs'

    def __iter__(self):
        yield self

    # def connect_to(self, other):
    #     self.outputs.append(other)
    #     other.inputs.append(self)

class NeuronLayer(list, Connectable):
    def __init__(self, name: str, count: int) -> None:
        super().__init__()
        self.name = name
        for x in range(0, count):
            self.append(Neuron(f'{name}-{x}'))

    def __str__(self) -> str:
        return f'{self.name} with ' \
            f'{len(self)} neurons' 


if __name__ == "__main__":
    n1 = Neuron("n1")
    n2 = Neuron("n2")
    l1 = NeuronLayer("l1", 3)
    l2 = NeuronLayer("l2", 4)

    n1.connect_to(n2)
    n1.connect_to(l1)
    l1.connect_to(n2)
    l1.connect_to(l2)

    print(n1)
    print(n2)
    print(l1)
    print(l2)
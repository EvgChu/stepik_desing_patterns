import sys
from copy import deepcopy

def is_singleton(factory):
    obj1 = factory()
    obj2 = factory()
    return obj1 is obj2

#код ниже руками не трогать:
obj = "1 2 3".split()
res1 = is_singleton(lambda:obj)
res2 = is_singleton(lambda:deepcopy(obj))

print(f'{res1} {res2}')
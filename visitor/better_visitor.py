
from abc import ABC

def _qualname(obj):
    """Get the fully-qualified name of an object (including module)."""
    return obj.__module__ + '.' + obj.__qualname__

def _declaring_class(obj):
    """Get the name of the class that declared an objects."""
    name = _qualname(obj)
    return name[:name.rfind('.')]

# Stored the actial visitor methods
_methods = {}

# Delegating visitor implamentation
def _visitor_impl(self, arg):
    """ Actual visitor method implementation. """
    method = _methods[(_qualname(type(self)), type(arg))]
    return method(self, arg)

def visitor(arg_type):
    """ Decorator that creates a visitor method."""

    def decorator(fn):
        declaring_class = _declaring_class(fn)
        _methods[(declaring_class, arg_type)] = fn
        return _visitor_impl
    return decorator


class DoubleExpression:
    def __init__(self, value) -> None:
        self.value = value

class AdditionExpression:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

class SubtractionExpression:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

class ExpressionPrinter:
    def __init__(self) -> None:
        self.buffer = []

    @visitor(DoubleExpression)
    def visit(self, de):
        self.buffer.append(str(de.value))

    @visitor(AdditionExpression)
    def visit(self, ae):
            self.buffer.append('(') 
            # ae.left.accept(self)
            self.visit(ae.left)
            self.buffer.append(' + ') 
            # ae.right.accept(self)
            self.visit(ae.right)
            self.buffer.append(')')

    @visitor(SubtractionExpression)
    def visit(self, ae):
            self.buffer.append('(') 
            # ae.left.accept(self)
            self.visit(ae.left)
            self.buffer.append(' - ') 
            # ae.right.accept(self)
            self.visit(ae.right)
            self.buffer.append(')')
 
    def __str__(self) -> str:
        return ''.join(self.buffer)

class ExpressionEvaluator:
    def __init__(self) -> None:
        self.value = None

    @visitor(DoubleExpression)
    def visit(self, de):
        self.value = de.value

    @visitor(AdditionExpression)
    def visit(self, ae):
        self.visit(ae.left)
        tmp = self.value
        self.visit(ae.right)
        self.value += tmp

    @visitor(SubtractionExpression)
    def visit(self, ae):
        self.visit(ae.left)
        tmp = self.value
        self.visit(ae.right)
        self.value = tmp - self.value
 
    def __str__(self) -> str:
        return f'= {self.value}' 

 
 
if __name__ == "__main__":
    e = AdditionExpression(
        DoubleExpression(5),
        SubtractionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    buffer = []
    printer = ExpressionPrinter()
    ee = ExpressionEvaluator()
    printer.visit(e)
    ee.visit(e)
    print(printer, ee) 
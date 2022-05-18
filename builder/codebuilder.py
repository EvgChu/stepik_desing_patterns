import sys

class CodeElement:
    indent_size = 2
    def __init__(self, name='') -> None:
        self.name = name.strip() 
        self.elements = []

    def __str__(self):
        lines = ["class " + self.name + ":"] 
        if not self.elements:
            str_pass = ' ' * (self.indent_size) + 'pass'
            lines.append(str_pass) 
        else:
            str_init = ' ' * (self.indent_size) + "def __init__(self):"
            lines.append(str_init)
            for field in self.elements:
                i = ' ' * (self.indent_size*2)
                i += "self." + field[0].strip() 
                i += " = " + field[1].strip()
                lines.append(i)
        return '\n'.join(lines)

# ваше решение
class CodeBuilder:
    def __init__(self, root_name):
        self.code = CodeElement(root_name)

    def add_field(self, type, name):
        self.code.elements.append( (type, name) )
        return self

    def __str__(self):
        return str(self.code)



def test_CodeBuilder():
    
    input_args = 'myclass, field1:20, field2:"22"'.split(',')
    cb = CodeBuilder(input_args[0])
    cb.add_field(input_args[1].split(':')[0], input_args[1].split(':')[1])
    cb.add_field(input_args[2].split(':')[0], input_args[2].split(':')[1])
    print(str(cb))
    input_args = ['myclass2']
    cb2 = CodeBuilder(input_args[0])
    print(str(cb2))


test_CodeBuilder()
import sys

# ваше решение
class CodeBuilder:
    def __init__(self, root_name):
        # todo
        pass

    def add_field(self, type, name):
        # todo
        pass

    def __str__(self):
        # todo
         
        return ""



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
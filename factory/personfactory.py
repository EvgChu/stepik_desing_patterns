import sys

"""
Дан класс Person. У него есть два атрибута: id и name .

Реализуйте PersonFactory с не статическим методом create_person(),
 который принимает имя человека и возвращет экземпляр класс Person с этим 
 именем и id. Поле id должно начинаться с нуля. То есть, фабрика вернёт п
 ервый экземпляр с id = 0, второй с id = 1 и так далее.
"""

class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory:
    def create_person(self, name):
        pass

#код ниже трогать не надо
names = sys.stdin.read().split(',')
pf = PersonFactory()
p1 = pf.create_person(names[0])
p2 = pf.create_person(names[1])

print(f'{p1.name}:{p1.id};{p2.name}:{p2.id}')
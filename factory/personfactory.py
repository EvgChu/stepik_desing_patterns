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
    _id_cnt = 0
    def create_person(self, name):
        person = Person(self._id_cnt,name)
        PersonFactory._id_cnt += 1
        return person

#код ниже трогать не надо
names = "Chris,Susan".split(',')
pf = PersonFactory()
p1 = pf.create_person(names[0])
p2 = pf.create_person(names[1])



print(f'{p1.name}:{p1.id};{p2.name}:{p2.id}')
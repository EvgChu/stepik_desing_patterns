import copy


class Address:
    def __init__(self, city, streer_address, country) -> None:
        self.streer_address = streer_address
        self.city = city
        self.country = country
    
    def __str__(self) -> str:
        return f'{self.streer_address}, {self.city}, {self.country}'


class Person:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f'{self.name} lives at {self.address}'

class Employee:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f'{self.name} works at {self.address}'


class EmployeeFactory:
    main_office_employee = Employee('', Address('123 East Dr',"London","UK"))
    aux_office_employee = Employee('', Address('123b East Dr',"London","UK"))

    @staticmethod
    def __new_employee(proto, name, suite):
        result = copy.deepcopy(proto)
        result.name = name
        result.address = suite


    @staticmethod
    def new_main_office_employee(proto, name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee,
            name,
            suite
        )

    @staticmethod
    def new_aux_office_employee(proto, name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee,
            name,
            suite
        )
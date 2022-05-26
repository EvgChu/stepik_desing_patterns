class Car:
    def __init__(self, driver) -> None:
        self.driver = driver

    def drive(self):
        print(f'Car is being driven by {self.driver.name}')


class CarProxy:
    def __init__(self, driver) -> None:
        self.driver = driver
        self._car = Car(driver)

    def drive(self):
        if self.driver.age >= 16:
            self._car.drive()
        else:
            print(f'Driver too young')


class Driver:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


if __name__ == "__main__":
    driver = Driver('John', 10)
    car = CarProxy(driver)
    car.drive()
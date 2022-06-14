


class Event(list):
    def __call__(self, *args, **kwds):
        for item in self:
            item(*args, **kwds)


class PropertyObservable:
    def __init__(self) -> None:
        self.property_changed = Event()


class Person(PropertyObservable):
    def __init__(self, age=0) -> None:
        super().__init__()
        self._age = age 

    @property
    def can_vote(self):
        return self._age >= 18

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if self._age == value:
            return
        old_can_vote = self.can_vote
        self._age = value
        self.property_changed("age", value)
        if old_can_vote != self.can_vote:
            self.property_changed("can_vote", self.can_vote)


class TrafficAuthority:
    def __init__(self, person: Person) -> None:
        self.person = person
        person.property_changed.append(
            self.person_change
        )

    def person_change(self, name, value):
        if value < 16:
            print("Sorry, you still cannot drive")
        else:
            print('Okay, you can drive now')
            self.person.property_changed.remove(
                self.person_change
            )


if __name__ == "__main__":

    def person_change(name, value):
        if name == 'can_vote':
            print(f'Voting ability changed to {value}')

    person = Person(13)
    person.property_changed.append(
        person_change
    )
    tr = TrafficAuthority(person)
    for age in range(14, 20):
        print( f"Setting age to {age}")
        person.age = age
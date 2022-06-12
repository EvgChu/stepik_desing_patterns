

class CreatureBad:
    def __init__(self) -> None:
        self.strenght = 10
        self.agility = 10
        self.intelligence = 10

    @property
    def sum_of_stats(self):
        return self.intelligence + self.strenght + self.agility
    
    @property
    def max_stats(self):
        return max(self.intelligence, self.strenght, self.agility)
    
    @property
    def average_stat(self):
        return self.sum_of_stats / 3.0

class Creature:
    _streight = 0
    _intelligence = 1
    _agility = 2
    def __init__(self) -> None:
        self.stats = [10, 10, 10]

    @property
    def strenght(self):
        return self.strenght[self._streight]

    @strenght.setter
    def strenght(self, value):
        self.stats[self._streight] = value

    @property
    def intelligence(self):
        return self.strenght[self._intelligence]

    @intelligence.setter
    def intelligence(self, value):
        self.stats[self._intelligence] = value

    @property
    def agility(self):
        return self.strenght[self._agility]

    @agility.setter
    def agility(self, value):
        self.strenght[self._agility] = value

    @property
    def sum_of_stats(self):
        return sum(self.stats)

    @property
    def max_stats(self):
        return max(self.stats)
    
    @property
    def average_stat(self):
        return self.sum_of_stats / len(self.stats)

    
if __name__ == "__main__":
    pass

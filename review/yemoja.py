class Orisha(object):
    def __init__(self, name, function, ebo):
        self.name = name
        self.function = function
        self.ebo = ebo

class Yemoja(Orisha):
    def __init__(self, name, function, ebo, temper):
        super().__init__(name, function, ebo)
        self.temper = temper
    def returnTemper(self):
        return self.temper + ' is the temper of Yemoja'

yemoja = Yemoja('Olokun', 'Intuition/Subconscious', 'Fruit', 'Hot/Cool/Nourishment/Warrior')
print(yemoja.returnTemper())

class MapOdu(object):
    def __init__(self, first_leg, second_leg, interpretation):
        self.first_leg = first_leg
        self.second_leg = second_leg
        self.interpretation = interpretation

    def __str__(self):
        return self.first_leg, self.second_leg, self.interpretation

    def __repr__self(self):
        return self.first_leg, self.second_leg, self.interpretation

map_odu_1 = MapOdu('Osa', 'Okanran', 'An unexpected change leads to a new direction/opportunity.')

print(map_odu_1.__repr__)
print(map_odu_1.__str__())

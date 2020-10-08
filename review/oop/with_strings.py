class MapOdu(object):
    def __init__(self, first_leg, second_leg, interpretation):
        self.first_leg = first_leg
        self.second_leg = second_leg
        self.interpretation = interpretation

    def __str__(self):
        return '%d-%d-%d' % (self.first_leg, self.second_leg, self.interpretation)

    def __repr__self(self):
        return 'Date(%r,%r,%r)' % (self.first_leg, self.second_leg, self.interpretation)

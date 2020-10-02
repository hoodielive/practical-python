class A():
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def plot_name(self):
        return self.name
    def plot_age(self):
        return self.age

class B(A):
    def __init__(self, name):
        self.name = name
    def plot_name(self):
        name = super().plot_name()
        return name


name1 = A('Larry', 4)

name2 = B('Jovial')

print(name2.plot_name())

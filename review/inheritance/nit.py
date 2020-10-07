class Parent:
    def __init__(self, name):
        self.name = name
        print("Parent __init__", name)

class Child(Parent):
    def __init__(self):
        print("Child __init__")
        super().__init__("Ruby")

child_obj = Child()

parent_obj = Parent('Janbalt')

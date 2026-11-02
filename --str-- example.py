class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Dog named " + self.name

d = Dog("Rex")
print(d)        # Dog named Rex
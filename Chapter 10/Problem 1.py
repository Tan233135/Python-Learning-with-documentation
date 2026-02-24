class Programmer:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        print(self.name, self.position, self.salary)

x = Programmer("tanvir", "system design", 12000)

print(x.name,x.position,x.salary)
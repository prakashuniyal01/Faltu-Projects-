class Programmer:
    company = 'mobiloitte'
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("prakash", 20000, 300200)
print(p.company, p.name, p.pin , p.salary)
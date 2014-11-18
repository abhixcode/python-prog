class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
    
    def lastName(self):
        return self.name.split()[-1]
    
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
        
if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'Software Engineer')
    sue = Person('Sue Jones', 41, 40000, 'Hardware Engineer')
    print(bob.name, sue.pay)
        
    print(sue.lastName())
    sue.giveRaise(0.10)
    print(sue.pay)
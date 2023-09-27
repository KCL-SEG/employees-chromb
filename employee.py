"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        payTotal = self.salary + self.contract['hours']*self.contract['rate'] + self.commision['contracts']*self.commision['rate'] + self.bonus
        
        return payTotal

    def __str__(self):
        description = self.name + " works on a "
        if self.salary != 0:
            description += "monthly salary of " + str(self.salary)
        else:
            description += "contract of " + str(self.contract['hours']) + " hours at " + str(self.contract['rate']) + "/hour"
        if self.commision['contracts'] != 0:
            description += " and receives a commission for " + str(self.commision['contracts']) + " contract(s) at " + str(self.commision['rate']) + "/contract"
        if self.bonus != 0:
            description += " and receives a bonus commission of " + str(self.bonus)
        description += ".\nTheir total pay is " + str(self.get_pay()) + "."
        
        return description


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.salary = 4000
billie.contract = {'hours': 0, 'rate': 0}
billie.commision = {'contracts': 0, 'rate': 0}
billie.bonus = 0

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.salary = 0
charlie.contract = {'hours': 100, 'rate': 25}
charlie.commision = {'contracts': 0, 'rate': 0}
charlie.bonus = 0

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.salary = 3000
renee.contract = {'hours': 0, 'rate': 0}
renee.commision = {'contracts': 4, 'rate': 200}
renee.bonus = 0

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')
jan.salary = 0
jan.contract = {'hours': 150, 'rate': 25}
jan.commision = {'contracts': 3, 'rate': 220}
jan.bonus = 0

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')
robbie.salary = 2000
robbie.contract = {'hours': 0, 'rate': 0}
robbie.commision = {'contracts': 0, 'rate': 0}
robbie.bonus = 1500

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
ariel.salary = 0
ariel.contract = {'hours': 120, 'rate': 30}
ariel.commision = {'contracts': 0, 'rate': 0}
ariel.bonus = 600

print(billie.get_pay())
print(str(billie))
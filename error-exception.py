import sys

class Act:
    def __init__(self, num, dem):
        self.num = num
        self.dem = dem

    def fucksGiven(self):
        if self.num % self.dem == 0:
            return 'Fucks given.'
        else:
            return 'Nope.'

for i in range(5, -1, -1):
    amountOf = Act(120, i)
    try:
        print(amountOf.fucksGiven())
    except ZeroDivisionError as err:
        print('No more fucks given:', err)

class MoneyFmt:
    def __init__(self, amount):
        self.amount = amount

    def update(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'{self.amount}'


    def dollarize(self):
        if self.amount >= 0:
            return '${:,.2f}'.format(self.amount)
        else:
            return '-${:,.2f}'.format(abs(self.amount))

    def __str__(self):
        return f'{cash.dollarize()}'
        
cash = MoneyFmt(12345678.021)
print(cash)
cash.update(100000.4567)
print(cash)
cash.update(-0.3)
print(cash)
print(repr(cash))
class Accoutn:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Владелец счета: {self.owner}\n баланс счёта:    ${self.balance}'


    def deposit(self, dep_amt):
        self.balance += dep_amt
        print('Внесение выполнено!')

    def withdraw(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Снятие Выполнено!')
        else:
            print('Недостаточно средств!')

acct1 = Accoutn("Vlad", 100)


acct1.owner = 'Vlad'

acct1.balance = 100

acct1.deposit(50)

acct1.withdraw(75)

acct1.withdraw(500)
print(acct1)
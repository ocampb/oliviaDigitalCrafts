class bankAccount:
    def __init__(self, balance, accountNumber):
        self.balance = balance
        self.accountNumber = accountNumber

    def deposit (self, depot):
        self.balance = self.balance + depot

    def withdrawal (self, remove):
        self.balance = self.balance - remove
    
    def transfer_funds (self, accountForTransfer, transferAmount):
        self.withdrawal(transferAmount)
        accountForTransfer.deposit(transferAmount)
        



account1 = bankAccount(100, 12345)
account2 = bankAccount (200, 23456)
print(account1.balance, account1.accountNumber)
bankAccount.withdrawal(account1, 50)
print(account1.balance, account1.accountNumber)
bankAccount.transfer_funds(account1, account2, 25)
print(account1.balance, account2.balance)

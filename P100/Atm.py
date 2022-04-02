from http.client import CannotSendHeader


class atm (object):
    def __init__(self,cash,input):
        self.cash = cash
        self.input = input
    def CashWithdrawal(self):
        self.cash = self.cash - self.input
    def BalanceEnquiry(self):
        print(self.cash)
    def CashDeposit(self):
        self.cash = self.cash+ self.input
I = int(input("Enter How much to change value by :"))
ATM=atm(5000,I)


DepOrWith = input("D to Deposit, W to Withdraw")
if DepOrWith== "D" :
    ATM.CashDeposit()
if DepOrWith== "W" :
    ATM.CashWithdrawal()
ATM.BalanceEnquiry()


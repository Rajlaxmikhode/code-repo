
class BankAccount():
    def __init__(self,balance=0):
        self.transactions=[]
        self.balance=balance
    def deposit(self,amount):
        
        if amount>0:
            self.balance+=amount
            self.transactions.append(+amount)
        return self.balance
    def withdrawl(self,amount):
        
        if amount<=0:
            print("Invalid amount")
        elif amount<=self.balance:
            self.balance-=amount
            self.transactions.append(-amount)
        else:
            print("No balance")
        
    def print_statement(self):
        return self.transactions
        

        
obj=BankAccount()
obj.deposit(678)
obj.deposit(349)
obj.withdrawl(678)
print(obj.print_statement())
print("Balance: ",obj.balance)






        

      
    
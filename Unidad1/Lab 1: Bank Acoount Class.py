class BankAccount:
  def __init__(self, holdersname, __balance):
    self.holdersname = holdersname
    self.__balance = __balance

  def deposit(self, amount):
    if amount > 0:
      self.__balance += amount
      print(f"Deposit: {amount} correct")
    else:
      print("The Deposit is 0 or negative, its not valid")
  
  def withdraw(self, amount):
    if amount > self.__balance:
      print("Error: you do not substract more money that you have D:")
    elif amount <= 0:
      print("Error: The substraction of the money is minus to 0.")
    else:
      self.__balance -= amount
      print(f"Substract of  ${amount} aproved.")

  def check_balance(self):
      print(f"Your balance is : {self.__balance}")

account1 = BankAccount("Raúl Pérez", 5000)
account2 = BankAccount("Joel López", 3000)


print(f"Holder's name: {account1.holdersname}")
account1.check_balance()  
account1.deposit(1000)    
account1.withdraw(2000)   
account1.check_balance()


print(f"Holder's name: {account2.holdersname}")
account2.check_balance()  
account2.deposit(1000)    
account2.withdraw(2000)   
account2.check_balance()

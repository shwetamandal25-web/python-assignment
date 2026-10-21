# class Balance:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance


# account1 = Balance("shweta", 9000)
# account2 = Balance("shiwani", 1000)

# print(account1.name)
# print(account1.balance)

# print(account2.name)
# print(account2.balance)

# account1.balance = 10000
# print(account1.balance)
    
    
# class Account:

#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def PrintAccount(self):
#         print(self.name)
#         print(self.balance)

#     def Spend(self, amount):
#         if self.balance < amount:
#             print("STOP SPENDING .. you dont have money")
#         else:
#             self.balance -= amount

#     def WithdrawMoney(self, amount):
#         if self.balance < amount:
#             print("Insufficient balance")
#         else:
#             self.balance -= amount


# A1 = Account("Anjali", 10000000)
# A2 = Account("Deepa", 10000000)
# A3 = Account("shweta", 5000)

# A1.PrintAccount()
# A2.PrintAccount()
# A3.PrintAccount()

# A3.WithdrawMoney(200)
# A1.WithdrawMoney(300)
# A2.WithdrawMoney(500)

# A3.PrintAccount()
# A2.PrintAccount()
# A1.PrintAccount()




class Account:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def WithdrawMoney(self, amount):
        if self.balance < amount:
            print("stop spending")
        else:
            self.balance -= amount


A1 = Account("Anjali", 10000000)
A2 = Account("Deepa", 10000000)
A3 = Account("shweta", 5000)

A3.WithdrawMoney(200)
A1.WithdrawMoney(300)
A2.WithdrawMoney(500)
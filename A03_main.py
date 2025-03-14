"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Tarryn Bereznycky"


# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client

from bank_account import *
from datetime import date
from client.client import Client

# 2. Create a Client object with data of your choice.

client_ben = Client(1111, "Ben", "Johnson", "benjohnson@gmail.com")

# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.

bens_chequing_account = ChequingAccount(2222, 1111, 5000, date(2020, 6, 3), -100, 2)
bens_savings_account = SavingsAccount(3333, 1111, 20000, date(2020, 6, 5), 100)

# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).

bens_chequing_account.attach(client_ben)
bens_savings_account.attach(client_ben)

# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.

client_bob = Client(5555, "Bob", "Jablonski", "benjablonski@gmail.com")
bobs_savings_account = SavingsAccount(1212, 5555, 30000, date(2015, 4, 6), 100)

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

#Bens Savings Account
try:
    bens_savings_account.withdraw(11000.01)
except ValueError as e:
    print(e)


try:
    bens_savings_account.withdraw(8950)
except ValueError as e:
    print(e)


try:
    bens_savings_account.deposit(5000)
except ValueError as e:
    print(e)


try:
    bens_savings_account.withdraw(400)
except ValueError as e:
    print(e)


try:
    bens_savings_account.withdraw(11000.01)
except ValueError as e:
    print(e)


try:
    bens_savings_account.withdraw(8950)
except ValueError as e:
    print(e)


# Bens Chequing Account
try:
    bens_chequing_account.withdraw(4900)
except ValueError as e:
    print(e)


try:
    bens_chequing_account.withdraw(55)
except ValueError as e:
    print(e)


try:
    bens_chequing_account.deposit(55000)
except ValueError as e:
    print(e)


#Bob
try:
    bobs_savings_account.withdraw(400)
except ValueError as e:
    print(e)


try:
    bobs_savings_account.deposit(500)
except ValueError as e:
    print(e)


try:
    bobs_savings_account.withdraw(600)
except ValueError as e:
    print(e)



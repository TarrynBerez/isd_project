"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Tarryn Bereznycky"

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime

from bank_account import *
from datetime import date


# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
try:
    chequing_account = ChequingAccount(1001, 1111, -500, date(2023, 5, 5), -100, 0.10)
except ValueError as e:
    print(e)

# 3. Print the ChequingAccount created in step 2.
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.

try:
    print(str(chequing_account))
    print(chequing_account.get_service_charges())
except ValueError as e:
    print(e)



# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
# 4b. Print the ChequingAccount
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.

try:
    chequing_account.deposit(1100)
    print(chequing_account)
    print(chequing_account.get_service_charges())
except ValueError as e:
    print(e)

print("===================================================")

# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.

try:    
    savings_account = SavingsAccount(1001, 1111, 15000, date(2020, 2, 13), 1000 )
except ValueError as e:
    print(e)

# 6. Print the SavingsAccount created in step 5.
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
try:
    print(savings_account)
    print(savings_account.get_service_charges())
except ValueError as e:
    print(e)

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
# 7b. Print the SavingsAccount.
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.

try:
    chequing_account.withdraw(15500)
    print(savings_account)
    print(savings_account.get_service_charges())
except ValueError as e:
    print(e)
print("===================================================")

# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
try:
    investment_account = InvestmentAccount(1001, 1111, 15000, date(2020, 2, 2), 10)
except ValueError as e:
    print(e)

# 9a. Print the InvestmentAccount created in step 8.
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
try:
    print(investment_account)
    print(investment_account.get_service_charges())
except ValueError as e:
    print(e)

# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.

try:
    investment_account2 = InvestmentAccount(1012, 2222, 10000, date(2014, 7, 14), 10)
except ValueError as e:
    print(e)

# 11a. Print the InvestmentAccount created in step 10.
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.

try:
    print(investment_account2)
    print(investment_account2.get_service_charges())
except ValueError as e:
    print(e)

print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.

try:
    chequing_account.withdraw(40.5)
    savings_account.withdraw(0.5)
    investment_account.withdraw(10.5)
    investment_account2.withdraw(0.5)

except ValueError as e:
    print(e)



# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.

try:
    print(chequing_account)
    print(savings_account)
    print(investment_account)
    print(investment_account2)
except ValueError as e:
    print(e)
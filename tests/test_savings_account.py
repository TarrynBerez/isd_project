import unittest
from bank_account.savings_account import SavingsAccount
from datetime import date

class TestSavingsAccount(unittest.TestCase):

    #Init Tests
    def test_init_valid_input_attributes(self):
        expected_date = date(2025, 2, 9)
        savings_account = SavingsAccount(1001, 1111, 15000,
                                         expected_date, 10)
        
        self.assertEqual(1001, savings_account._BankAccount__account_number)
        self.assertEqual(1111, savings_account._BankAccount__client_number)
        self.assertEqual(15000, savings_account._BankAccount__balance)
        self.assertEqual(expected_date, savings_account._date_created)
        self.assertEqual(10, savings_account._SavingsAccount__minimum_balance)


    def test_init_minimum_balance_invalid_type(self):
        savings_account = SavingsAccount(1001, 1111, 15000,
                                         date(2025, 2, 9), "Ten")
        expected_result = 50
        self.assertEqual(expected_result, savings_account._SavingsAccount__minimum_balance)


    #Get Service Charges Tests
    def test_get_service_charges_balance_greater_than_minimum_balance(self):
        savings_account = SavingsAccount(1001, 1111, 15000,
                                         date(2025, 2, 9), 50)
        expected = 0.5
        self.assertEqual(expected, savings_account.get_service_charges())

    
    def test_get_service_charges_balance_equal_to_minimum_balance(self):
        savings_account = SavingsAccount(1001, 1111, 50,
                                         date(2025, 2, 9), 50)  
        expected = 0.5
        self.assertEqual(expected, savings_account.get_service_charges())  
    

    def test_get_service_charges_balance_less_than_minimum_balance(self):
        savings_account = SavingsAccount(1001, 1111, 10,
                                         date(2025, 2, 9), 50)  
        expected = 1.00

        self.assertEqual(expected, savings_account.get_service_charges())
        
        
    #__str__
    def test_str_appropriate_value_returned(self):
        savings_account = SavingsAccount(1001, 1111, 15000,
                                         date(2025, 2, 9), 50)

        expected = (f"Account Number: 1001 Balance: $15,000.00\n"
                    f"Minimum Balance: $50.00 Account Type: Savings")
        self.assertEqual(expected, str(savings_account))
        
"""
Description: Unit tests for the CheuqingAccount class.
Author: Tarryn Bereznycly
"""

import unittest
from bank_account.chequing_account import ChequingAccount
from datetime import date

class TestChequingAccount(unittest.TestCase):
    def test_init_valid_input_attributes(self):
        expected_date = date(2025, 2, 9)
        chequing_account = ChequingAccount(1001, 1111, 11000,
                                            date, 1000, 0.10)
        self.assertEqual(1001, chequing_account._BankAccount__account_number)
        self.assertEqual(1111, chequing_account._BankAccount__client_number)
        self.assertEqual(11000, chequing_account._BankAccount__balance)
        self.assertEqual(1000, chequing_account._ChequingAccount__overdraft_limit)
        self.assertEqual(0.10, chequing_account._ChequingAccount__overdraft_rate)
        self.assertEqual(expected_date, chequing_account._date_created)


    def test_init_invalid_overdraft_limit_type(self):
        expected_date = date(2025, 2, 8)
        chequing_account = ChequingAccount(1001, 1111, 11000, expected_date,
                                           "one hundred", 0.10)
        
        self.assertEqual(chequing_account._ChequingAccount__overdraft_limit, -100)


    def test_init_invalid_overdraft_rate_type(self):
        expected_date = date(2025, 2, 8)
        chequing_account = ChequingAccount(1001, 1111, 11000, expected_date,
                                           1000, "ten percent")
        
        self.assertEqual(chequing_account._ChequingAccount__overdraft_rate, 0.05)
        
    
    def test_init_invalid_date_type(self):
        expected_date = "Febuary 8th, 2025"
        chequing_account = ChequingAccount(1001, 1111, 11000, expected_date,
                                           1000, 0.10)
        
        self.assertEqual(date.today(), chequing_account._date_created)

    
    def test_get_services_charge_greater_than_balance(self):
        expected_date = date(2025, 2, 8)
        chequing_account = ChequingAccount(1001, 1111, 11000, expected_date,
                                           1000, 0.10)
        expected_result = 0.5
        self.assertEqual(expected_result, chequing_account.get_service_charges())


    def test_get_services_charge_less_than_balance(self):
        expected_date = date(2025, 2, 8)
        chequing_account = ChequingAccount(1001, 1111, 500, expected_date,
                                           1000, 0.10)

        expected_result = 50.5
        self.assertEqual(expected_result, chequing_account.get_service_charges())

    
    def test_get_services_charge_equal_to_balance(self):
        expected_date = date(2025, 2, 8)
        chequing_account = ChequingAccount(1001, 1111, 500, expected_date,
                                           500, 0.10)
        expected_result = 0.5
        self.assertEqual(expected_result, chequing_account.get_service_charges())


    def test_str_appropriate_value_returned(self):
        expected_date = date(2025, 2, 8)
        chequing_account = ChequingAccount(1001, 1111, 15000, expected_date,
                                           1000, 0.10)

        expected_result = (f"Account Number: 1001 Balance: $15,000.00\n"
        f"Overdraft Limit: $1,000.00 Overdraft Rate: 0.1% Account Type: Chequing")
        self.assertEqual(str(chequing_account), expected_result)
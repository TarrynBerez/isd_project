"""
Description: Unit tests for the InvestmentAccount class.
Author: Tarryn Bereznycky

"""

import unittest
from bank_account.investment_account import InvestmentAccount
from datetime import date

class TestInvestmentAccount(unittest.TestCase):

    def test_init_valid_attributes_set(self):

        #Init Tests
        investment_account = InvestmentAccount(1001, 1111, 15000,
                                               date(2025, 2, 9), 2.00)
        
        self.assertEqual(1001, investment_account._BankAccount__account_number)
        self.assertEqual(1111, investment_account._BankAccount__client_number)
        self.assertEqual(15000, investment_account._BankAccount__balance)
        self.assertEqual(date(2025, 2, 9), investment_account._date_created)
        self.assertEqual(2.00, investment_account._InvestmentAccount__management_fee)

    
    def test_init_management_fee_invalid_type(self):
        investment_account = InvestmentAccount(1001, 1111, 15000,
                                               date(2025, 2, 9), "Two Dollars")
        expected = 2.55
        self.assertEqual(investment_account._InvestmentAccount__management_fee, expected)
        

    #Get Service Charges Tests
    def test_get_service_charges_date_created_more_than_10_years_ago(self):
        investment_account = InvestmentAccount(1001, 1111, 15000,
                                               date(2014, 2, 9), 10)
        expected = 0.50

        self.assertEqual(expected, investment_account.get_service_charges())


    def test_get_service_charges_date_created_equal_to_ten_years_ago(self):
        investment_account = InvestmentAccount(1001, 1111, 15000,
                                                date(2015, 2, 9), 10)
        expected = 0.5
        self.assertEqual(expected, investment_account.get_service_charges())


    def test_get_service_charges_date_created_within_10_years(self):
        investment_account = InvestmentAccount(1001, 1111, 15000,
                                                date(2020, 2, 9), 10)
        expected = 10.5
        
        self.assertEqual(expected, investment_account.get_service_charges())

    #__str__
    def test_str_approptiate_value_returned_created_less_than_10_years_ago(self):
        investment_account = InvestmentAccount(1001, 1111, 15000,
                                                date(2025, 2, 9), 10)
        
        expected = (f"Account_number: 1001 Balance: $15,000.00\n"
                    f"Date Created: 2025-02-09 Management Fee: Waived Account Type: Investment")
        self.assertEqual(expected, str(investment_account))


    def test_str_approptiate_value_returned_created_more_than_10_years_ago(self):
        investment_account = InvestmentAccount(1001, 1111, 15000,
                                                date(2015, 1, 9), 10)
        expected = (f"Account_number: 1001 Balance: $15,000.00\n"
                    f"Date Created: 2015-01-09 Management Fee: $10.00 Account Type: Investment")
        self.assertEqual(expected, str(investment_account))
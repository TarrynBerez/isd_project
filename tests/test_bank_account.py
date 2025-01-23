"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""
import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.bankAccount = BankAccount(1111, 2222, 40000)


    #Init Tests
    def test_init_valid_input_attributes(self):
        bankAccount = BankAccount(1111, 2222, 40000)

        self.assertEqual(1111, bankAccount._BankAccount__account_number)
        self.assertEqual(2222, bankAccount._BankAccount__client_number)
        self.assertEqual(40000, bankAccount._BankAccount__balance)


    def test_init_invalid_account_number_raises_value_error(self):
        with self.assertRaises(ValueError):
            BankAccount("1111", 2222, 40000)
    

    def test_init_invalid_client_number_raises_value_error(self):
        with self.assertRaises(ValueError):
            BankAccount(1111, "2222", 40000)


    def test_init_invalid_balance_set_to_0(self):
        expected = BankAccount(1111, 2222, "4O000")
        actual = BankAccount(1111, 2222, 0)

        self.assertEqual(expected.balance, actual.balance)
    

    #account_number tests
    def test_account_number_accessor_valid_returns_account_number_attribute(self):
        self.assertEqual(self.bankAccount.account_number, 1111)

    
    def test_client_number_accessor_valid_returns_client_number_attribute(self):
        self.assertEqual(self.bankAccount.client_number, 2222)


    def test_balance_accessor_valid_returns_balance_attribute(self):
        self.assertEqual(self.bankAccount.balance, 40000)


    #Update Balance Tests
    def test_update_balance_correctly_updates_balance_positive_amount(self):
        self.bankAccount.update_balance(4000)
        self.assertEqual(self.bankAccount.balance, 44000)


    def test_update_balance_correcty_updates_balance_negative_amount(self):
        self.bankAccount.update_balance(-10000)
        self.assertEqual(self.bankAccount.balance, 30000)
    

    def test_update_balance_remains_unchanged_if_amount_non_numeric(self):
        self.bankAccount.update_balance("One Thousand")
        self.assertEqual(self.bankAccount.balance, 40000)


    #Deposit Tests
    def test_deposit_updates_balance_valid_amount(self):
        self.bankAccount.deposit(40000)
        self.assertEqual(self.bankAccount.balance, 80000)

    
    def test_depost_negative_amount_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.bankAccount.deposit(-40000)

    
    #Withdraw Tests
    def test_withdraw_updates_balance_valid_amount(self):
        self.bankAccount.withdraw(30000)
        self.assertEqual(self.bankAccount.balance, 10000)

    
    def test_withdraw_negative_amount_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.bankAccount.withdraw(-40000)


    def test_withdraw_amount_exeeds_balance_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.bankAccount.withdraw(50000)

    
    def test_str_valid_returns_str_method(self):
        expected = f"Account Number: 1111 Balance: $40,000.00"
        self.assertEqual(expected, str(self.bankAccount))
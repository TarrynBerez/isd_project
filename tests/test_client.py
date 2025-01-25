"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""
import unittest
from client.client import Client

class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Client(1111, "Tarryn", "Bereznycky", "email@gmail.com")


    #Init Tests
    def test_init_valid_input_attributes(self):
        client = Client(1111,"Tarryn", "Bereznycky", 
                        "email@gmail.com")
        

        self.assertEqual(1111, client._Client__client_number)
        self.assertEqual("Tarryn", client._Client__first_name)
        self.assertEqual("Bereznycky", client._Client__last_name)
        self.assertEqual("email@gmail.com", client._Client__email_address)

    
    def test_init_invalid_client_number_raises_value_error(self):
        with self.assertRaises(ValueError):
            Client("1111", "Tarryn", "Bereznycky", "email@gmail.com")
        

    def test_init_blank_first_name_raises_value_error(self):
        with self.assertRaises(ValueError):
            Client(1111, " ", "Bereznycky", "email@gmail.com")


    def test_init_blank_last_name_raises_value_error(self):
        with self.assertRaises(ValueError):
            Client(1111, "Tarryn", " ", "email@gmail.com")


    def test_init_invalid_email_sets_default_email(self):
        expected = Client(1111, "Tarryn", "Bereznycky", "email@pixell-river.com")
        actual = Client(1111, "Tarryn", "Bereznycky", "22")
        self.assertEqual(expected.email_address, actual.email_address)


    #Valid Return Tests
    def test_client_number_accessor_valid_returns_client_number_attribute(self):
        self.assertEqual(self.client.client_number, 1111)
    

    def test_first_name_accessor_valid_returns_first_name_attribute(self):
        self.assertEqual(self.client.first_name, "Tarryn")
    

    def test_last_name_accessor_valid_returns_last_name_attribute(self):
        self.assertEqual(self.client.last_name, "Bereznycky")


    def test_email_address_accessor_valid_returns_email_adress_attribute(self):
        self.assertEqual(self.client.email_address, "email@gmail.com")


    def test_str_valid_returns_str_method(self):
        expected = "Bereznycky, Tarryn [1111] - email@gmail.com"
        self.assertEqual(expected, str(self.client))

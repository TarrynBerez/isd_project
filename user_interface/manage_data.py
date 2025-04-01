__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Tarryn Bereznycky"

import os
import sys
# THIS LINE IS NEEDED SO THAT THE GIVEN TESTING 
# CODE CAN RUN FROM THIS DIRECTORY.
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import csv
from datetime import datetime
import logging

from client.client import Client
from bank_account import *

from datetime import date

# *******************************************************************************
# GIVEN LOGGING AND FILE ACCESS CODE
 
# Absolute path to root of directory
root_dir = os.path.dirname(os.path.dirname(__file__))
 
# Path to the log directory relative to the root directory
log_dir = os.path.join(root_dir, 'logs')
 
# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok = True)
 
# Specify the path to the log file within the log directory
log_file_path = os.path.join(log_dir, 'manage_data.log')
 
# Configure logging to use the specified log file
logging.basicConfig(filename=log_file_path, filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s\n\n')
 
# Given File Path Code:
# Designed to locate the input files without providing any directory structure

# Construct the absolute path to the data directory at the root of the project
data_dir = os.path.join(root_dir, 'data')
 
# Construct the absolute paths to the data files
clients_csv_path = os.path.join(data_dir, 'clients.csv')
accounts_csv_path = os.path.join(data_dir, 'accounts.csv')
 
# END GIVEN LOGGING AND FILE ACCESS CODE
# *******************************************************************************

def load_data()->tuple[dict,dict]:
    """
    Populates a client dictionary and an account dictionary with 
    corresponding data from files within the data directory.
    Returns:
        tuple containing client dictionary and account dictionary.
    """
    client_listing = {}
    accounts = {}

    # READ CLIENT DATA 
    with open(clients_csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        try:
            for value in reader:
                client_data = Client(int(value["client_number"]), str(value["first_name"]),
                                str(value["last_name"]),     str(value["email_address"]))
                
                client_listing[client_data.client_number] = client_data
                
        except ValueError as e:
            logging.error(f"Unable to create client: {str(e)}")
            
        

    # READ ACCOUNT DATA
    with open(accounts_csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for value in reader:
            try:  
                date = datetime.strptime(value["date_created"], "%Y-%m-%d").date()
                if str(value["account_type"]) == "ChequingAccount":
                    account_data = ChequingAccount(int(value["account_number"]), int(value["client_number"]), float(value["balance"]),
                                            date, float(value["overdraft_limit"]), float(value["overdraft_rate"]))
                    
                elif str(value["account_type"]) == "InvestmentAccount":
                    account_data = InvestmentAccount(int(value["account_number"]), int(value["client_number"]), float(value["balance"]),
                                            date, float(value["management_fee"]))
                
                elif str(value["account_type"]) == "SavingsAccount":
                    account_data = SavingsAccount(int(value["account_number"]),    int(value["client_number"]), 
                                                  float(value["balance"]), date, float(value["minimum_balance"]))
                else:                 
                    raise ValueError("Not a valid account_type")
                    
                if account_data.client_number not in client_listing.keys():
                    logging.error(f"{str(account_data.client_number)} contains invalid Client Number {str(account_data.client_number)}")
                else:
                    accounts[account_data.account_number] = account_data
                
            except ValueError as e:
                logging.error(f"Unable to create bank account: {str(e)}")

    # RETURN STATEMENT
    return (client_listing, accounts)


def update_data(updated_account: BankAccount) -> None:
    """
    A function to update the accounts.csv file with balance 
    data provided in the BankAccount argument.
    Args:
        updated_account (BankAccount): A bank account containing an updated balance.
    """
    updated_rows = []

    with open(accounts_csv_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames
        
        for row in reader:
            account_number = int(row['account_number'])
            # Check if the account number is in the dictionary
            if account_number == updated_account.account_number:
                # Update the balance column with the new balance from the dictionary
                row['balance'] = updated_account.balance
            updated_rows.append(row)

    # Write the updated data back to the CSV
    with open(accounts_csv_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(updated_rows)

# GIVEN TESTING SECTION:
if __name__ == "__main__":
    clients,accounts = load_data()

    print("=========================================")
    for client in clients.values():
        print(client)
        print(f"{client.client_number} Accounts\n=============")
        for account in accounts.values():
            if account.client_number == client.client_number:
                print(f"{account}\n")
        print("=========================================")
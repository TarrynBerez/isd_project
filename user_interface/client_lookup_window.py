__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Tarryn Bereznycky"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """
    Aa window for looking up client information and their accounts.
    
    """
    def __init__(self):
        """
        Initializes the ClientLookupWindow.
        
        """
        super().__init__()
            
        data = load_data()
        self.__client_listing = data[0]
        self.__accounts = data[1]
        
        self.lookup_button.clicked.connect(self.__on_lookup_client)
        self.client_number_edit.textChanged.connect(self.__on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)
        
    @Slot()
    def __on_lookup_client(self):
        """
        Retrieves and displays information for hte specified client.
        
        """
        try:
            client_number = int(self.client_number_edit.text())
        except:
            QMessageBox.information(self, "Input Error", "The client number must be a numeric value.") 
            self.reset_display()
            return
     
        if client_number not in self.__client_listing.keys():
            QMessageBox.information(self, "Not Found", f"Client number: {client_number} not found.") 
            self.reset_display()
            return
        else:
            self.client_info_label.setText(f"Client Name: {self.__client_listing[client_number].first_name} "
                                           f"{self.__client_listing[client_number].last_name}")    
                   
            for account in self.__accounts.items():
                if account[1].client_number == client_number:              
                    row_position = self.account_table.rowCount()
                    self.account_table.insertRow(row_position)
                    
                    account_number_item = QTableWidgetItem(str(account[1].account_number))
                    account_number_item.setTextAlignment(Qt.AlignCenter)
                    
                    balance_item = QTableWidgetItem(QTableWidgetItem(f"${account[1].balance:,.2f}"))
                    balance_item.setTextAlignment(Qt.AlignRight)
                    
                    date_created_item = QTableWidgetItem(str(account[1]._date_created))
                    date_created_item.setTextAlignment(Qt.AlignCenter)
                    
                    account_item = QTableWidgetItem(account[1].__class__.__name__)
                    account_item.setTextAlignment(Qt.AlignCenter)
                    
                    self.account_table.setItem(row_position, 0, account_number_item)
                    self.account_table.setItem(row_position, 1, balance_item)
                    self.account_table.setItem(row_position, 2, date_created_item)
                    self.account_table.setItem(row_position, 3, account_item)
                    self.account_table.resizeColumnsToContents()
    
    @Slot()
    def __on_text_changed(self):
        """
        Clears all table rows when the text in the box changes.
        
        """
        self.account_table.setRowCount(0)
    
    
    @Slot(int, int)
    def __on_select_account(self, row : int, column : int):
        """
        Handles the selection of an account in the account table.
        
        args:
            row (int):
                The row of the selected cell
                
            column (int):
                The column of the selected cell
            
        """
        selected_account = self.account_table.item(row, 0).text()
        
        if len(selected_account.strip()) != 0:
            if int(selected_account) in self.__accounts.keys():
                for account in self.__accounts.items():
                    if account[1].account_number == int(selected_account):
                        account_window = AccountDetailsWindow(account[1])
                        account_window.balance_updated.connect(self.__update_data)
                        account_window.exec()   
                                          
            elif selected_account not in self.__accounts.keys():
                QMessageBox.information(self, "No Bank Account", "Bank Account selected does not exist.")       
        else:
            QMessageBox.information(self, "Invalid Selection", "Please select a valid record.")
            
    
    @Slot(BankAccount)
    def __update_data(self, account : BankAccount):
        """
        Updates the valance of hte specified amount in hte acount table.
        
        Args:
            account (BankAccount):
                The account object containing the account number and updated balance.
        
        """
        for row in range(self.account_table.rowCount()):
            if int(self.account_table.item(row, 0).text()) == int(account.account_number):
                self.account_table.setItem(row, 1, QTableWidgetItem(f"{account.balance:,.2f}"))                                 
                
        self.__accounts[account.account_number] = account
        update_data(account)     
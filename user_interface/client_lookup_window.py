__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot



from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """
    Docstring!
    
    """
    def __init__(self):
        """
        Docstring!
        
        """
        super().__init__()
            
        data = load_data()
        self.client_listing = data[0]
        self.accounts = data[1]
        
        self.lookup_button.clicked.connect(self.__on_lookup_client)
        self.client_number_edit.textChanged.connect(self.__on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)
        
        
    def __on_lookup_client(self):
        """
        Docstring!
        
        """
        try:
            client_number = int(self.client_number_edit.text())
        except:
            QMessageBox.information(self, "Input Error", "The client number must be a numeric value.") 
            self.reset_display()
             
        if client_number not in self.client_listing.keys():
            QMessageBox.information(self, "Not Found", f"Client number: {client_number} not found.") 
            self.reset_display()
            return
        else:
            
            self.client_info_label.setText(f"Client Name: {self.client_listing[client_number].first_name} "
                                           f"{self.client_listing[client_number].last_name}") 
            
            for account in self.accounts.items():
                if account[1].client_number == client_number: ##Trying to get it to pull client number from accounts
                    
                    row_position = self.account_table.rowCount()
                    self.account_table.insertRow(row_position)
                    
                    
                    self.account_table.setItem(row_position, 0, QTableWidgetItem(str(account[1].account_number)))
                    self.account_table.setItem(row_position, 1, QTableWidgetItem(f"{account[1].balance:,.2f}"))
                    self.account_table.setItem(row_position, 2, QTableWidgetItem(str(account[1]._date_created)))
                    self.account_table.setItem(row_position, 3, QTableWidgetItem(account[1].__class__.__name__))
                    self.account_table.resizeColumnsToContents()
    
    def __on_text_changed(self):
        """
        Docstring!
        
        """
        pass
    
    @Slot(int, int)
    def __on_select_account(self, row : int, column : int):
        """
        Docstring

        """
        selected_account = self.account_table.item(row, 0).text()
        if len(selected_account.strip()) != 0:
            if int(selected_account) in self.accounts.keys():
                for account in self.accounts.items():
                    if account[1].account_number == int(selected_account):
                        account_window = AccountDetailsWindow(account[1])
                        account_window.exec()   
                                          
            elif selected_account not in self.accounts.keys():
                QMessageBox.information(self, "No Bank Account", "Bank Account selected does not exist.")       
        else:
            QMessageBox.information(self, "Invalid Selection", "Please select a valid record.")
            
    
    def __update_data(self):
        """
        Docstring!
        
        """
        pass
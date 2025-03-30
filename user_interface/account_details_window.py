__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Tarryn Bereznycky"

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """
    balance_updated = Signal(BankAccount)
    
    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        super().__init__()
        
        self.__account = account
        
        self.account_number_label.setText(str(account.account_number))
        self.balance_label.setText(f"${account.balance:,.2f}")
        
        self.deposit_button.clicked.connect(self.__on_apply_transaction)
        self.withdraw_button.clicked.connect(self.__on_apply_transaction)
        self.exit_button.clicked.connect(self.__on_exit)
        
        if isinstance(self.__account, BankAccount) == False:
            self.reject()


    def __on_apply_transaction(self):
        try:
            amount = float(self.transaction_amount_edit.text())
        except:
            QMessageBox.information(self, "Invalid Data", "Amount must be numeric.")
            self.transaction_amount_edit.setFocus()
            return
    
        try:
            sender = self.sender()
            
            if sender == self.deposit_button:
                transaction_type = "Deposit"
                self.__account.deposit(amount)
                
            elif sender == self.withdraw_button:
                transaction_type = "Withdraw"
                self.__account.withdraw(amount)
                
            self.balance_label.setText(str(self.__account.balance))
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()
            
        except Exception as e:
            QMessageBox.information(self, f"{transaction_type} Failed", str(e))
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

        self.balance_updated.emit(self.__account)
        
        
    def __on_exit(self):
        self.close()
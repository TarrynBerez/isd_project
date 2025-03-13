# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.


## Author
Tarryn Bereznycky


## Encapsulation
In the bank account class encapsulation was achieved by making the account_number, client_number, and balance so they are
only accessible in the class. Also methods like update_balance, deposit and withdraw were added to interact with and update the balance.


## Assignment
Assignment 1: We created a bank account and client class and incorperated encapsulation through the use of private attributes, public accessors and mutators.
Assignment 2: In this assignment we used abstraction, inheritance and polymorphism to create a chequing, investment, and savings account.
Assignment 3: We used strategy patterns to implement a system for calculating service charges and observers for notifying the account owner of any issues


## Polymorphism
Polymorphism was achieved in the subclasses by using the super init to initialize attributes inherited from the bank account class and each
subclass having unique implementation to the get_service_charges method and __ str__.


## Strategy Pattern
The strategy pattern is being used to define different ways to calculate service charges for a BankAccount class.
"We Gonna have 2 Classes in these code one that handles the Customer data , second is Its Bank Details Data"

class Customer:

    def __init__(self, name, address , phone ): # <--- Class One 

        self.name = name

        self.address = address


        self.phone = phone


        self.accounts = []


    def add_account(self, account):
            self.accounts.append(account)

    def get_account_balance(self):

            total_balance = 0

            for account in self.accounts:

                total_balance += account.balance


                return total_balance
            


class BankAccount:     #<--------- Classs Two

    def __init__(self, account_number, customer):

        self.account_number = account_number


        self.customer = customer

        self.balance = 0



    def deposit(self, amount):
        self.balance += amount



    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

        else:
            print("Insufficient funds!")


    def get_account_info(self):
        return "Account Number: {}\nCustomer Address: {}\nCustomer Phone: {}\nBalance: {}".format(self.account_number, self.customer.name, self.customer.address, self.customer.phone, self.balance)
    



customer1 = Customer("Rafay Khan", "Piperd Michead Compound (kurla)", "8097877216") # <--- Calling Customer Beta here 


customer2 = Customer("Asim Khan", "Nagpada Temkar Molla Bombay","9233532322")


account1 = BankAccount("001", customer1) # <--- Calling Bank Betaa here


account2 = BankAccount("002",customer2)

account3 = BankAccount("003", customer2)


account1.deposit(1000)

account1.withdraw(500)

account2.deposit(2000)

account3.deposit(1500)

account3.withdraw(200)


customer1.add_account(account1)

customer1.add_account(account2)

customer2.add_account(account3)

print("")
print("{} Total Balance: {}".format(customer1.name, customer1.get_account_balance()))
print("")
print("{} Total Balance: {}".format(customer2.name, customer2.get_account_balance()))
print("")
print(account1.get_account_info())
print("")
print(account3.get_account_info())




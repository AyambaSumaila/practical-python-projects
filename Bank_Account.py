class SavingsAccount:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
        self.total_deposits = 0
        self.total_withdrawals = 0
        self.monthly_service_charges = 0

    def deposit(self, amount):
        self.balance += amount
        self.total_deposits += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.total_withdrawals += amount
        else:
            print("\t\t\tInsufficient funds!")

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest

    def deduct_monthly_charge(self):
        self.balance -= self.monthly_service_charges


class CheckingAccount:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
        self.total_deposits = 0
        self.total_withdrawals = 0
        self.monthly_service_charges = 0

    def deposit(self, amount):
        self.balance += amount
        self.total_deposits += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.total_withdrawals += amount
        else:
            print("\t\t\tInsufficient funds!")

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest

    def deduct_monthly_charge(self):
        self.balance -= self.monthly_service_charges


def main():
    # Create a savings account
    savings_account = SavingsAccount(1000, 0.05)

    # Create a checking account
    checking_account = CheckingAccount(500, 0.02)

    # Get the user's input
    while True:
        print()
        print("\t\t\tSelect from the following choices:")
        print()
        
        print("\t\t\t1. Deposit to savings account.")
        print()
        
        print("\t\t\t2. Withdraw from savings account.")
        print()
        
        print("\t\t\t3. Deposit to checking account.")
        print()
        
        print("\t\t\t4. Withdraw from checking account.")
        print()
        
        print("\t\t\t5. Quit.")

        choice = input()

        if choice == "1":
            amount = int(input("\t\t\tEnter the amount to deposit: "))
            savings_account.deposit(amount)
        elif choice == "2":
            amount = int(input("\t\t\tEnter the amount to withdraw: "))
            savings_account.withdraw(amount)
        elif choice == "3":
            amount = int(input("\t\t\tEnter the amount to deposit: "))
            checking_account.deposit(amount)
        elif choice == "4":
            amount = int(input("\t\t\tEnter the amount to withdraw: "))
            checking_account.withdraw(amount)
        else:
            break

    # Apply interest and deduct service charges for the month
    savings_account.apply_interest()
    checking_account.apply_interest()
    savings_account.deduct_monthly_charge()
    checking_account.deduct_monthly_charge()

    # Print the statistics for the month
    print("\t\t\tSavings account:")
    print("\t\t\tBeginning balance: $", savings_account.balance)
    print("\t\t\tTotal deposits: $", savings_account.total_deposits)
    print("\t\t\tTotal withdrawals: $", savings_account.total_withdrawals)
    print("\t\t\tService charges: $", savings_account.monthly_service_charges)
    print("\t\t\tEnding balance: $", savings_account.balance)

    print("\t\t\tChecking account:")
    print("\t\t\tBeginning balance: $", checking_account.balance)
    print("\t\t\tTotal deposits: $", checking_account.total_deposits)
    print("\t\t\tTotal withdrawals: $", checking_account.total_withdrawals)
    print("\t\t\tService charges: $", checking_account.monthly_service_charges)
    print("\t\t\tEnding balance: $", checking_account.balance)

    return 0


if __name__ == "__main__":
    main()


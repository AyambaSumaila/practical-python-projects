class BankAcount:
    def __init__(self, bal):

    def  deposit(self, amount):
        self.__balance +=amount

        def withdraw(self, amount):
            if self.__balance >=amount:
                self.__balance -=amount

            else:
                print('Error: Insufficient funds')

        def get_balance(self):

            def __str__(self):
                return 'The balance is $'+format(self.__balance, ', .2f')

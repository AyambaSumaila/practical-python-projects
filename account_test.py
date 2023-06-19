import bankacount

def main():
    start_bal=float(input('Enter your starting balance:'))
    savings=bankaccount.BankAccount(start_bal)
    pay=float(input('How much were you paid week?'))
    print('I will deposit that into account.')
    savings.deposit(pay)
    print('Your account balance is $  , '  (savings.get_balance(), ', .2f'), sep='')
    cash=float(input('How much would you like to withdraw? '))
    print('I will withdraw that from account.')
    saving.withdraw(cash)

    print('Your account balance is $', \format(savings.get_balance(), ', .2f'), sep='')

    main()


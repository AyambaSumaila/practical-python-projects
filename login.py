import login
def main():
    first=input('Enter your first name: ')
    second=input('Your Second name:')
    idNumber=input('Enter your student ID number:')
    print('Your login name is: ')
    print(login.get_login_name(first, second, idNumber))

def get_login_name(firstName, lastName, idnum):
    set=firstName[0 :  3]
    set2=lastName[0 : 3]
    set3=idnum[-3 : ]
    login_name=set+set2+set3
    return login_name
main()
import login_student

def main():
    password=input('Enter your password: ')
    while not login_student.validate_password(password):
        print('That password is not valid!.')
        password=input('Enter your password:')
    print('That is a valid password.')
main()
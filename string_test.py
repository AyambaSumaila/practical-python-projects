
def main():
            user_string=input('Enter a string: ')
            print('This is what I found about that string:')

            if  user_string.isalnum():
                print('String is alphanumeric.')
            if user_string.isdigit():
                print('The string contains only digits.')
            if user_string.isalpha():
                print('The string contains only alphabetic characters.')
            if user_string.isspace():
                print('The string contains only whitespace characters')
            if user_string.islower():
                print('The letters contains in the string are all lowercase')
           if  user_string.isupper():
               print('The letters in the string are all uppercase.')

main()



def get_login_name(first, last, idnum):
     set=first[0:3]
     set2=last[0:3]
     set3=idnum[-3:]
     login_name=set+set2+set3

     return login_name

def validate_password(password):
     correct_pass_leng=False
     pas_has_upperccase=False
     pas_has_lowercase=False
     pas_has_digit=False

     if len(password)>=7:
          correct_pass_leng=True
          for ch in password:
               if ch.islower():
                    pas_has_lowercase=True
               if ch.isdigit():
                    pas_has_digit=True
               if correct_pass_leng and pas_has_upperccase and pas_has_lowercase and pas_has_digit:
                    is_valid=True
               else:
                    is_valid=False
               return is_valid






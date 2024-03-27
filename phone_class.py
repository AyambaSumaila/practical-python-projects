class Phone:
    def __init__(self, brand, model_name, price):
        self.brand=brand
        self.model_name=model_name
        self.price=price
        
        
        @staticmethod
        def make_a_call(phone_number):
            print(f'calling {phone_number}')
            
            
        def full_name(self):
            
            return f'{self.brand} {self.model_name}'
        
        
        
class Date:
    def __init__(self, year, month, day):
        self.year=year
        self.month=month
        self.day=day
        
    def arrange_value_into_Date_pattern(self):
        date=str(self.day) + '-' + str(self.month) + '-' + str(self.year)
        return date
    
    @classmethod
    def getDataformString(clr, string):
        import re
        data = re.findall('\d{2}-\d{2}-\d{4}|\d{2}/\d{2}/\d{4}',string)[0]
        list_date= data.replace('/','-').split('-')
        print(list_date)
        day =  list_date[0]
        month =  list_date[1]
        year =  list_date[2]
        return clr(year,month,day)
    
    @staticmethod     # 2022-06-17 ---> 17-06-2022
    def setDatePattern(string):
        list1 = string.replace('/','-').split('-')
        print(list1)
        date_update = list1[2] + '-' + list1[1]  + '-' + list1[0]
        return date_update
    
    
phone=Phone('Techno', 10, 1992)

print(phone.__dict__)
print(phone.make_a_call('00000'))

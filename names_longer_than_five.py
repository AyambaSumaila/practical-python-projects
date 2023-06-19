def longer_than_five(list_of_names):
    for name in list_of_names:
        if len(name) >5:
            return True
    return False
list1=["Samuel", "John", "Paul", "Ghana", "Daudaw"]
list2=["Georgee", "Wahabu", "Benjamin"]
list3=["Ge", "Wah", "Ben"]
print(longer_than_five(list1))
print(longer_than_five(list2))
print(longer_than_five(list3))
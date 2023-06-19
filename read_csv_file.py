fileCon=open("grades.txt", "r")
lines=fileCon.readlines()
for lin in lines:
    print(lin.strip())
print("------------")
header=lines[0]

field_name=header.strip().split(',')
print(field_name)
for row in lines[:5]:
    vals=row.strip().split(',')
    if vals[9] !="NA":
        print("{}: {}; {}".format(vals[0], vals[3], val[4]))
        
    
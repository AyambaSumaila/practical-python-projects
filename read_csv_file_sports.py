sports_persons=[("Messi", 36, "Footballer"),
             ("Federrer", 37, "Tennis"),
            ("Tiger", 46, "Golf"),
            ("Alonso", 27, "Cyclying"),
            ("Ramos", 17, "Gymnastics")]

out_file=open('myScocers.csv', 'r')
#out_file.write(('Name, Age, Sport'))
#out_file.read('\n')


header_row='Name, Age, Sport'
print("===== Sports personalities ======")
print(header_row)
for sport in sports_persons:
    out_file.read([sport])
out_file.close()
sports_persons=[("Messi", 36, "Footballer"),
             ("Federrer", 37, "Tennis"),
            ("Tiger", 46, "Golf"),
            ("Alonso", 27, "Cyclying"),
            ("Ramos", 17, "Gymnastics")]

out_file=open('myScocers.csv', 'w')
out_file.write(('Name, Age, Sport'))
out_file.write('\n')


header_row='Name, Age, Sport'
print("===== Sports personalities ======")
print(header_row)
for sport in sports_persons:
    row_string='{}, {}, {}'.format(sport[0], sport[1],
                                   sport[2])
    out_file.write(row_string)
    out_file.write('\n')
out_file.close()

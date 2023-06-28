import os

with open('planets.txt', 'r') as f:
     for lines in f:
         file_name, file_ext=(os.path.splitext(lines))
         file_title, file_course, file_num=file_name.split('-')
         file_title=file_title.strip()
         file_course=file_course.strip()
         file_num=file_num.strip()[1:].zfill(2)
                 
         new_name='{}-{}-{}'.format(file_num, file_title, file_ext)
         a=os.rename(f.tostring(), new_name)
         print(a)
    

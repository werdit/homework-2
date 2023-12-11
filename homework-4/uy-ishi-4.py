"""
1.ls
2.touch
    enter filename: test.txt
    enter data: " bu yerda yozilgan
                  data test.txt ga yozilishi kerak
                  end
                  "
3.mkdir
    enter fodername: asror
4.cd
    enter foldername: folder1 / .. :
5.mv [optional]
    enter filename: test.txt folder/test1.txt
6.\q


 test1/
    file1.txt
    file2.txt
    file3.txt
 test2/
    file1.txt
    file2.txt
    file3.txt
test3/
    file1.txt
    file2.txt
    file3.txt
test4/
    file1.txt
    file2.txt
    file3.txt
"""


import os
import time

while True:
    a = input()
    if a=='ls':
        contents = os.listdir()
        print(contents)
    elif a=='touch':
        b=input('enter filename: ')
        c=input('enter data: ')
        with open(b, "w") as f:
            f.write(c)
        print(f'{b} named file created, you can see after \q')
    elif a=='mkdir':
        d=input('enter foldername: ')
        os.makedirs(d)
        print(f'{d} named folder created, you can see after \q')
        time.sleep(1)
    if a=='cd':
        e=input('enter foldername: ')
        if e=='..':
            os.chdir('..')
        else:
            os.chdir(f"C:/Users/user/PycharmProjects/pythonProject/{e}")
    elif a != '\q' and a != 'cd' and a!= 'mkdir' and a != 'ls' and a != 'touch':
        print("There is not such a command")
        break
    elif a=='\q':
        break

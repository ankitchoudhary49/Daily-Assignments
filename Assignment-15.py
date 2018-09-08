#Question 1: Create a Databse of Students


import sqlite3
try:
    con=sqlite3.connect('Students.db')  
    cursor=con.cursor()
    query='create table students(name varchar(20),roll_no int(5), class varchar (5), age int(2), marks int(2))'
    cursor.execute(query)
    print('Table created ')
    con.commit()
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done')


#Question 2: Take Students Name and Marks From the User
    
try:
    con=sqlite3.connect('Students.db')
    cursor=con.cursor()
    query='create table students(name varchar(20) primary key, marks int(3))'
    cursor.execute(query)
    print('Table created')
    con.commit()
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done!')
a=[]
i=0
while(i<10):
    try:
        name=input("Enter the name of the student: ")  
        marks=int(input('Enter the marks of the student: '))      
        if(marks<0 or marks >100):
            raise ValueError('Invalid entry of marks.')
            i=i-1
        else:
            t=name,marks
            a.append(t)
            i=i+1
    except  ValueError as ve:
        print(ve)

#Question 3: Append the Values in 2 Columns
        
try:
    con=sqlite3.connect('Students.db')
    cursor=con.cursor()
    query="insert into students(name, marks) values(?,?)"
    records=a
    cursor.executemany(query, records)
    con.commit()
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done!')

#Question 4: Print the names of all the students who scored more than 80 marks
    
import sqlite3
try:
    con=sqlite3.connect('Students.db')
    cursor=con.cursor()
    query='select * from students where marks>80'    
    cursor.execute(query)
    data=cursor.fetchall()
    for row in data:
        print('Name: {}'.format(row[0]))
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done!')

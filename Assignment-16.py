#Assignment 16

#Question 1: Take Students Name and Marks From the User

import pymongo
client=pymongo.MongoClient()
database=client['Students']
collection=database['student_collection']

#Question 2: Append the Values in 2 Columns

for i in range(10):
    try:
        name=input("Enter name:-") 
        marks=int(input('Enter  Marks:-'))
        if(marks<0 or marks >100):  
            raise ValueError('Invalid entry')
            i=i-1
    except ValueError as msg:
        print(msg)
        
#Question 3: Create a Databse of Students
        
for i in range(10):
    try:
        name=input("Enter name: ") 
        marks  int(input('Enter  Marks:-'))
        if(marks<0 or marks >100):  
            raise ValueError('Invalid entry')
            i=i-1
        else:
            collection.insert_one({'Name':-name,'Marks':-marks})  
            i=i+1
    except ValueError as msg:
        print(msg)

#Question 4: Print the names of all the students who scored more than 80 marks
        
db=collection.find({"Marks":{"$gt":80}})
for data in db:
    print(data)

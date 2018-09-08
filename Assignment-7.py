#Assignment-7

#Question1: Get Keys Corresponding to a Value in User Defined Dictionary

d={}
noele=int(input("Enter the number of elements of the dictionary:"))
for i in range(noele):
    key=input("Enter the key: ")
    value=input("Enter the value: ")
    d[key]=value
print(d.values())

#Question 2: Nested Dictionary

dict_student1={'name':'Aman', 'marks':{'english':80,'maths':85,'physics':90,'Chemistry':83}}
dict_student2={'name':'Amit', 'marks':{'english':81,'Maths':90,'physics':91,'Chemistry':85}}
dict_student3={'name':'Ram', 'marks':{'english':82,'Maths':87,'physics':92,'Chemistry':87}}
dict_student4={'name':'Laxman', 'marks':{'english':87,'Maths':86,'physics':97,'Chemistry':90}}
name=input("Enter name of the student: ")

if name=='Aman':
        print(dict_student1['marks'])
if name=='Amit':
    print(dict_student2['marks'])
if name=='Ram':
    print(dict_student3['marks'])
if name=='Laxman':
    print(dict_student4['marks'])
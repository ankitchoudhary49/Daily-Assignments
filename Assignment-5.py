#Assignment 5

#Question 1: Verify leap year

year=int(input("Enter the year:\n"))
if year%4==0 or year%400==0 and year%100==0:
    print("This year is a leap year.\n")
else:
    print("This is not a leap year")

print("*"*50)

#Question 2: Check Whether the Given Dimensions Are of Square or Rectangle

length=int(input("Enter the length:\t"))
breadth=int(input("Enter the breadth:\t"))
if length==breadth:
            print("It is a square.")
else:
             print("It is a rectangle.")
print("*"*50)

#Question 3: Determine Oldest and the Youngest Age
age1=int(input("Enter age of the first person:\t"))
age2=int(input("Enter age of the second person:\t"))
age3=int(input("Enter age of the third person:\t"))
if age1>age2 and age1>age3:
    print("Age of the first person i.e. {} is greater.".format(age1))
elif age2>age1 and age2>age3:
    print("Age of the second person i.e. {} is greater.".format(age2))
elif age3>age1 and age3>age1:
    print("Age of the third person i.e. {} is greater.".format(age3))
else:
    print("All three people are of the same age.")

print("*"*50)


'''Question 4: Analyse the Given Data:
            Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service. 

            1. if employee is female, then she will work only in urban areas. 
            2. if employee is a male and age is in between 20 to 40 then he may work in anywhere 
            3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only. 
            4. And any other input of age should print "ERROR". 
'''

age=int(input("Enter age of the person:\t"))
sex=input("Enter sex of the person (M/F):\t")
mstat=input("Enter marital status of the person (Y/N):\t")
    

if sex=='f' or sex=='F':
    print("The employee will work only in urban areas.")
    
if sex=='m' or sex=='M':
    if age<20 or age>60:
        print("ERROR")
    elif age>=20 and age<40:
        print("The employee will work anywhere.")
    elif age>=40 and age<=60:
        print("The employee will work only in urban areas.")

print("*"*50)


#Question 5: Cost Problem

quant=int(input("Enter the quantity of the item:  "))
cost=quant*100
if cost>1000:
    cost=cost-((cost*10)/100)
print("The total amount customer has to pay is {}.".format(cost))

print("*"*50)

#Question 6: Print User Defined Integers

i=0
new_list=[]
while i<10:
    num=int(input("Enter a number:  "))
    i+=1
    new_list.append(num)
    #print("Entered value: {}".format(num))
print(new_list) #print(','.join(new_list)) is not working.
print("*"*50)

#Question 7: Write An Infinite Loop.
''''j=0
while j>=0:
    print("This is an infinite loop.")
    j+=1
print("*"*50)    '''    
#Question 8: Make a List Which Will Store Square of Elements of Other List.


ele1=int(input("Enter 5 elements of the list:\n"))
ele2=int(input())
ele3=int(input())
ele4=int(input())
ele5=int(input())
lst=[ele1,ele2,ele3,ele4,ele5]
l=[]
for i in lst:
    l1=i*i
    l.append(l1)
print(l)

print("*"*50)

#Question 9: Group the all Data Types in a List.

list1=[1,2,45,'hey','hello',12.8,13.9]
list_int=[]
list_str=[]
list_float=[]
for i in list1:
    if type(i)==int:
        list_int.append(i)
    elif type(i)==str:
        list_str.append(i)
    elif type(i)==float:
        list_float.append(i)
    else:
        print("Invalid data type.")

print("List of integers: {}\nList of float: {}\nList of Strings: {}".format(list_int,list_float,list_str))
print("*"*50)  

#Question 10: Make a List Containing Prime Numbers.

list_prime=[]
for i in range(1,101):
    if i%2==0:
        list_prime.append(i)
print("List of prime numbers: {}".format(list_prime))

print("*"*50)  

#Question 11: Pattern.

i=1
while i<5:
    print('*'*i)
    i+=1
print("*"*50)  

#Question 12: Search and Delete an Element from a User Defined List.

element1=int(input("Enter elements of the list:\n"))
element2=int(input())
element3=int(input())
element4=int(input())
element5=int(input())
element6=int(input())
listl=[element1,element2,element3,element4,element5,element6]
delel=int(input("Enter an element to be deleted:\n"))
found=0
for i in listl:
    if i==delel:
        found=1
        listl.remove(i)
        break
    if found==1:
        listl.remove(i)
if found==0:
    print("Element not found.")
print(listl)
print("*"*50)





















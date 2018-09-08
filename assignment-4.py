#Asignment 4

#Question 1: Reverse the List.

print("*"*50)

list1=[1,2,3,4,5]
print(list1[::-1])  #list1.reverse() was not working so i had to use slice operator.

print("*"*50)

#Question 2: Extract all the uppercase letters from a string.

str1='My name is ANKIT CHOUDHARY.'
for i in str1:
    if i.isupper()==True:
        print(i,end='  ')
print("\n")

print("*"*50)

#Question 3: Split and Store the Values After TypeCasting.

str2=input("Enter a string:\n")
str3=str2.split(',')
print(str3)
lst=[]
for i in str3:
    l=int(i)
    lst.append(l)
print(lst)

print("*"*50)

#Question 4: Check for Palindrome.

str4=input("Enter a string:\n")
if str4==str4[::-1]:
    print("String is a palindrome.")
else:   
    print("String is not palindrome.")

print("*"*50)

#Question 5: Understand Deep and Shallow Copy.

import copy as c
lst1=[1,2,[3,4],5]
lst2=c.deepcopy(lst1)
print(lst2)

print("*"*50)
'''
Difference between shallow and deep copy:
Shallow copy - if original object contains any reference to mutable objects, then the duplicate preferance variables will be created
               pointing to old containing object but no duplicate objects gets created.
Deep copy - A deep copy constructs a new compound object and then, recursively inserts copies into it of the objects found in the original.
'''    

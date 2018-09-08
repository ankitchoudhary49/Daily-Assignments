#Question 1: Create a list with user defined inputs.


print('*'*50)
ele1=input('Enter the elements of list \n')
ele2=input()
ele3=input()
ele4=input()
ele5=input()

list1=[ele1,ele2,ele3,ele4,ele5]

print(list1)
print('*'*50)

'''
Question 2: Add the following list11 to above created list1:
[‘google’,’apple’,’facebook’,’microsoft’,’tesla’]

'''

list1.append('google')
list1.append('apple')
list1.append('facebook')
list1.append('microsoft')
list1.append('tesla')

print(list1)

print('*'*50)

#Question 3: Count the number of time an object occurs in a list1.

list1.append('apple')
print(list1.count('apple'))
print('*'*50)

#Question 4: create a list1 with numbers and sort it in ascending order.

list1=[1,4,2,5,7,4,2,3,2,54,34,4,6,23,9]
list1.sort()
print(list1)
print('*'*50)


'''
Question 5: Given are two one-dimensional arrays A and B which are sorted in ascending order.
Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [list1]
'''

A=['1','2','3','4']
B=['6','7','8','9']
C=A+B
C.sort()
print(C)
print('*'*50)



#Question 6: Count even and odd numbers in a list1.

list2=['1','2','3','4','5','6','7','8','9']
counteven=0
countodd=0
for j in list2:
    if(int (j)%2==0):
        counteven+=1
    else:
        countodd+=1

print('Number of even digits are %d and number of odd digits are %d.'%(counteven,countodd))

print("*"*50)


#Question 7: Print a Tuple in Reverse Order.


t=(1,2,3,4,5,6)
print(t[::-1])

print("*"*50)

#Question 8: Find largest and smallest elements of a tuple.

print(max(t))
print(min(t))

print("*"*50)

#Question 9: Convert a string to uppercase.

string1='This string is printed in uppercase1'
print(string1.upper())

print("*"*50)


#Question 10: Check If the String Contains All Numeric Characters.


string2='1234567890'
print(string2)
if (string2.isdigit()==True):
    print("The sting contains all numbers")
else:
    print("The string does not contain all numeric characters.")

print("*"*50)


#Question 11: Replce the Given String With Your Name.


string3='This string needs to be replaced.'
print(string3)
print(string3.replace(string3,'Ankit Choudhary'))


print("*"*50)










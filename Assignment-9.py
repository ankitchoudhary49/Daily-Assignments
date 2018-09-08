#Assignment 9
'''
Question 1:Name and handle the exception occured in the following program: 

a=3
if a<4:
    a=a/(a-3)
    print(a)
'''
#Exception: ZeroDivisionError
a=3
if a<4:
    try:
        a=a/(a-3)
    except:
        a=int(input("please enter a value other than 3. "))
    a=a/(a-3)
    print(a)
'''
Question 2: Name and handle the exception occurred in the following program: 
l=[1,2,3] 
print(l[3])
'''
#Exception: IndexError

l=[1,2,3]
try:
    print(l[3])
except:
    l1=int(input("Enter an index smaller than 3. "))
    if l1<3:
        print(l[l1])
'''
Question 3: What will be the output of the following code:

# Program to depict Raising Exception
     
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")
    raise  # To determine whether the exception was raised or not
'''
#The above code will print a NameError.

#Question 4: What will be the output of the following code: 

# Function which returns a/b
def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

'''
output: -5.0
        a/b result in 0
'''
'''
#Question 5: Write a program to show and handle following exceptions: 
1. Import Error 
2. Value Error 
3. Index Error
'''

try:
    print(sys.version)
except:
    print("Import Error")
try:
    z=int(input("Enter any value other than int to see if it produces an error or not. "))
except ValueError:
    z=int(input("Now enter an integer value. "))
    print(z)
l=[1,2,3,4,5]
try:
    print(l[8])
except IndexError:
    y=int(input("Enter an index less than 4. "))
    if(y<5):
        print(l[y])
    

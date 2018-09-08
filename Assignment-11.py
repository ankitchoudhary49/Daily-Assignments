#Assignment 11

#Question 1: Write a python code to find a valid email address from a text.

import re
counter=0
mail=input("Enter an email address: ")
check=re.finditer('^[\w][_.a-zA-Z0-9]*[@](gmail.com|yahoo.com)$',mail)
for c in check:
    counter+=1
    print("E-mail id {1} is found at {0} index\n".format(c.start(),c.group()))
if counter==0:
    print("Please enter a valid E-mail id.")
print("*"*50)

#Question 2: Write a python program to find a valid Indian phone number from a text.(Valid Indian numbers will start with "+91-" and after that [6-9] followed by 9 digits. )

number=input("Enter a phone number with country code: ")
check1=re.finditer('[+][9][1][6-9][0-9]{9}',number)
count=0
for ch in check1:
    count+=1
    print("Phone number {} is found at the index {}.".format(ch.start(),ch.group())) 
if count==0:
    print("Invalid phone number found.")


#Assignment 12
#Question 1: Print the Current Day

import datetime
print(datetime.date.today())
x=datetime.date.today()
print("OR")
print(x.strftime("%A, %B %d,%Y"))

print("*"*50)
#Question 2: Use Webbrowser Module in Python
'''
import webbrowser

google=input("Enter your google search here: ")
webbrowser.open_new_tab("https://www.google.co.in/search?btnG=1&q=%s"%google)
'''
#Question 3: Rename All the Files in a Directory And Convert Them Into .jpg File Format

import os
print(os.getcwd())
os.rename('Empty file 1.txt','file 1.jpg')
os.rename('Empty file 2.txt','file 2.jpg')

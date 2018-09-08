#Assignment 10

#Question 1: Write a Python program to read n lines of a file

#Suppose we have to read 2 lines of the file

f=open('test.txt','r')
cnt=0
while cnt<2:
    data=f.readline()
    print(data)
    cnt=cnt+1
f.close()

#Question 2: Write a Python program to count the frequency of words in a file.

g=open('test.txt','r')
q=g.read()
n=input("Enter word to check frequency: ")
b=q.count(n)
print("{} occurs {} times ".format(n,b))

#Question 3: Write a Python program to copy the contents of a file to another file.

with open("test.txt",'r+') as h:
    with open("test1.txt", "r+") as j:
        for line in h:
            j.write(line)

#Question 4: Write a Python program to combine each line from first file with the corresponding line in second file.

with open('test.txt','r') as i:
    with open('test1.txt', 'r+') as k:
        for line in i:
            line=i.readline()
            k.write(line)

#Question 5: Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.

lst=[]
f1=open('test.txt','w+')
for x in range(0,10):
    num=int(input("Enter a value: "))
    lst.append(num)
f2=open('test2.txt','a')
f2.write(str(lst))
print(lst)
lst.sort()
f1.write(str(lst))
f1.close()
f1=open('test.txt','r')
b=f1.read()
print(b)

f1.close()
f2.close()


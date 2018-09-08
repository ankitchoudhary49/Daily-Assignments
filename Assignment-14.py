#Assignment 14

#Question 1: Print the Cube of Each Value of a List
lst=[1,2,3,4,5]
lst_cube=[i*i*i for i in lst]
print(lst_cube)
print("*"*50)

#Question 2: Get all the Prime Numbers in a Specific Range
lst1=[x for x in range(2, 20) if all(x % y != 0 for y in range(2, x))]
print(lst1)
print("*"*50)

#Question 3: Differentiate Between List Comprehension and Generator Expression
'''
The generator yields one item at a time and generates item only when in demand. Whereas, in a list comprehension, Python reserves memory for the whole list.
Thus we can say that the generator expressions are memory efficient than the lists.
'''

#Question 4: Convert the Python List to Fahrenheit

celsius = [39.2, 36.5, 37.3, 37.8]
faren=[]
far = lambda temp : temp * 9/5 + 32
for j in celsius:
    faren.append(far(j))
print(faren)
print("*"*50)

#Question 5: Square all the Elements of a List
s_lst=[1,2,3,4,5]
sq_lst=[]
lam_sq = lambda n : n*n
for k in s_lst:
    sq_lst.append(lam_sq(k))
print(sq_lst)

print("*"*50)


#Question 6: Filter out all the primes from a list

lis=[0,1,2,3,4,5,6,7,8,9,10]
p=list(filter(lambda l : l%2==0, lis))
print(p)
print("*"*50)

#Question 7: Multiply all the Elements of a List
lst_1=[1,2,3,4,5,6 ]
lst_2=[7,8,9,10,11,]
lst_3=list(map(lambda d,e:d*e,lst_1,lst_2))

print(lst_3)
print("*"*50)

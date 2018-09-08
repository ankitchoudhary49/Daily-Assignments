#Assignment 8

#Question 1: Calculate Area and Circumference of a Circle.
class circle:
    def getarea(self,radius):
        self.area=3.14*radius*radius
        return self.area
    def getcircum(self,radius):
        self.circum=2*3.14*radius
        return self.circum

radius=int(input("Enter the radius of the circle: "))
c=circle()
area=c.getarea(radius)
circumference=c.getcircum(radius)
print("Area of the circle is {} and circumference of the circle is {}.".format(area,circumference))

#Question 2: Make a Class Student and Display its Required Info

class student:
    def info(self):
        self.rollno=int(input("Enter the roll number of the student:\n"))
        self.name=input("Enter the name of the student:\n")
        self.marks=int(input("Enter marks of the student:\n"))
    def in_age(self):
        self.age=int(input("Enter age of the studnet:\n"))
    def display(self):
        print("Roll number of the student is {}, his name is {}, he has scored {} and his age is {}".format(self.rollno,self.name,self.marks,self.age))
s=student()
s.info()
s.in_age()
s.display()

#Question 3: Convert Temperature

class temperature:
    def convertFahrenheit(self):
        self.cel=int(input("Enter temperature in celcius to convert it into farenheit:\n"))
        self.far=self.cel*9/5+32
        print("{} in celcius is equal to {} in farenheit.".format(self.cel,self.far))
    def convertCelsius(self):
        self.farenheit=int(input("Enter temperature in farenheit to convert it into celcius:\n"))
        self.celcius=((self.farenheit - 32))
        self.celcius=self.celcius*(5/9)
        print("{} in farenheit is equal to {} in celcius.".format(self.farenheit,self.celcius))
t=temperature()
t.convertFahrenheit()
t.convertCelsius()


#Question 4: Create a Class MovieDetails and Perform the Required Functionalities
class MovieDetails:
    def MovieInfo(self):
        self.artistName=input("Enter tha name of artist of the movie:\n")
        self.year=int(input("Enter the release year of the movie:\n"))
        self.rating=int(input("Enter ratings of movie (out of 5):\n"))
    def Display(self):
        print("Name of artist is {}, release year of the movie is {} and it is rated {} out of 5 ".format(self.artistName,self.year,self.rating))
    def add(self):
        self.dir=input("Enter name of the director of the movie:\n")
        self.producer=input("Enter name of the producer of the movie:\n")

MD=MovieDetails()
MD.MovieInfo()
MD.Display()
MD.add()

#Question 5: Inheritance(Animal)

class animal:
    def animal_attribute(self):
        print("This is a method of the base class.")
class tiger(animal):
    def method(self):
        print("This is method of the derived class.")
tig=tiger()
tig.animal_attribute()

#Question 6: Determine the Output
'''
class A:
    def f(self):
        return self.g()

    def g(self):
         return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print(a.f(), b.f())
print(a.g(), b.g())
'''
'''
Output:
A B
A B
'''

#Question 7: Inheritance(Shapes)
class shape:
    def input(self):
        self.length=int(input("Enter the length:\n"))
        self.breadth=int(input("Enter the breadth:\n"))
    def area(self):
        self.ar=(self.length)*(self.breadth)
        if(self.length==self.breadth):
            print("Area of this square is {}".format(self.ar))
        else:
            print("Area of this rectangle is {}".format(self.ar))
class square(shape):
    def inp(self):
        self.length=int(input("Enter the length:\n"))
        self.breadth=int(input("Enter the breadth:\n"))
        a=area(length,breadth)
        print(a)
class rectangle(shape):
    def inp(self):
        self.length=int(input("Enter the length:\n"))
        self.breadth=int(input("Enter the breadth:\n"))
        
s=square()
r=rectangle()
s.input()
s.area()
r.input()
r.area()

    
        

















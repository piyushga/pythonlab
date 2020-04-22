#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[4]:


class Triangle:
    a=0.0
    b=0.0
    c=0.0
    def create_triangle(self):
        self.a=float(input("Enter the first side of the triangle"))
        self.b=float(input("Enter the second side of the triangle"))
        self.c=float(input("Enter the third side of the triangle"))
    def print_sides(self):
        print("First side is",self.a)
        print("Second side is",self.b)
        print("Third side is",self.c)
t1=Triangle()
t1.create_triangle()
t1.print_sides()    


# In[7]:


class String:
    def get_string(self):
        self.a=input("Enter a string: ")
    def print_string(self):                         
        print("The Entered String is ",self.a) 
obj=String()
obj.get_string()                
obj.print_string()


# In[10]:


class String:
    def get_string(self):
        self.a=input("Enter a string: ")
        return(self.a)
obj=String()
print("The Eentered String is ",obj.get_string())


# In[16]:


class Rectangle:
    l=0.0
    w=0.0
    def perimeter(self, len, wid):
        self.l=len
        self.w=wid
        return(2*self.l*self.w)
obj=Rectangle()
print("The Perimeter of the rectangle is ",obj.perimeter(5,20))


# In[20]:


class Circle:
    def __init__(self, radius):
        self.r=radius
    def perimeter(self):
        return(2*3.14*self.r)
    def area(self):
        return(3.14*self.r*self.r)
obj=Circle(10)
print("The Circumference of the circle is ",obj.perimeter())
print("The arae of the circle is ",obj.area())
    


# In[1]:


class Circle:
    r=0.0
    def __init__(self):
        self.r=float(input("Enter radius:"))
    def perimeter(self):
        return(2*3.14*self.r)
    def area(self):
        return(3.14*self.r*self.r)
obj=Circle()
print("The Circumference of the circle is ",obj.perimeter())
print("The arae of the circle is ",obj.area())
    


# In[37]:


class Temperature:
    f=0.0
    c=0.0
    def convert_fahrenheit(self):
        self.c=float(input("ENter celsius Temperature:"))
        return((1.8*self.c)+32)
    def convert_celsius(self):
        self.f=float(input("ENter Fahrenheit Temperature:"))
        return((self.f-32)/1.8)
obj=Temperature()
print("The conversion from celsius to fahrenheit is:",obj.convert_fahrenheit())
print("The conversion from fahrenheit to celsius is:",obj.convert_celsius())


# In[5]:


class Student:
    Name=""
    Roll_no=""
    Age=0
    Marks=0
    def __init__(self, name, roll_no):
        self.Name=name
        self.Roll_no=roll_no
    def set_age(self):
        self.Age=int(input("Enter the Age:"))
    def set_marks(self):
        self.Marks=int(input("Enter the Marks:"))
    def display(self):
        return self.Name,self.Age,self.Roll_no,self.Marks 
obj= Student("Piyush","2K18CSUN01072")
obj.set_marks()
obj.set_age()
print("The details of the student are:",obj.display())


# In[2]:


class Time:
    hr1=0
    min1=0
    hr2=0
    min2=0
    thr=0
    tmin=0
    def add_time(self):
        self.hr1=int(input("Enter the no.of hrs:"))
        self.min1=int(input("Enter the no.of mins:"))
        self.hr2=int(input("Enter the no.of hrs:"))
        self.min2=int(input("Enter the no.of mins:"))
        self.thr=self.hr1+self.hr2
        self.tmin=self.min1+self.min2
        if(self.tmin>60):
            self.thr=self.thr+(int(self.tmin/60))
            self.tmin=self.tmin%60
    def display_time(self):
        print("Time is",self.thr,"",self.tmin)
    def display_tmin(self):
        print("Total Minutes are:",60*self.thr+self.tmin)
    
obj=Time()
obj.add_time()
obj.display_time()
obj.display_tmin()        

    


# In[6]:


class reversestring:
    a=""
    def rev_function(self):
        self.a=input("Enter a string:")
        return self.a[::-1]
rev=reversestring()
print("Reverse string is",rev.rev_function())


# In[ ]:





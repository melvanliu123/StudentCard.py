from Student import Student
from Date import Date
n= input()
m= int(input())
d= int(input())
y= int(input())

b1=Date(6, 1, 1999)
b2=Date(10, 8, 1997)
s1=Student("John", b1, 90) 
s2=Student("Marry", b2, 80)


s1.setName(n)
s2.setDate(Date(m,d,y))
s1.toString()
s2.toString()

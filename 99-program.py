import os
os.system('cls')

def rectangle(l,b) :
    area=l*b
    return area

def sqaure(a):
    area2=a*a
    return area2

l=input("Enter the length of rectangle : ")
b=input("Enter the breadth of rectangle : ")
l=int(l)
b=int(b)
r=rectangle(l,b)
print("Area of rectangle is",r)    

side=input("Enter the side of square : ")
side=int(side)
s=sqaure(side)
print("Area of square is "+str(s))    
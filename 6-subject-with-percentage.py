#karan's program for calculate total and percentage of 6 subject marks.
a=int(input("Enter bioinfo:"))
b=int(input("Enter perl:"))
c=int(input("Enter eng:"))
d=int(input("Enter c++:"))
e=int(input("Enter HTML:"))
f=int(input("Enter css:"))
T=a+b+c+d+e+f
Per=(T/600)*100
print("Total marks:",T)
print("Percentage:",Per)

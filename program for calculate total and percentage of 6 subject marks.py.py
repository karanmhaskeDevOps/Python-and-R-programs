#karan's program for calculate total and percentage of 6 subject marks.
a=int(input("Enter C/C++:"))
b=int(input("Enter Java:"))
c=int(input("Enter Perl:"))
d=int(input("Enter Juliya:"))
e=int(input("Enter R:"))
f=int(input("Enter Python:"))
T=a+b+c+d+e+f
Per=(T/600)*100
print("Total marks:",T)
print("Percentage:",Per)

if Per >= 85:
    print("garde is A")
elif Per >=75:
    print("grade is B")
elif Per >=65:
    print("grade is c")
elif Per >=55:
    print("grade is d")
elif Per >= 35:
    print("student is fail")
    

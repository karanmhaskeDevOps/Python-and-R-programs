#karan ,python program for tuple sort

l=[]
n=int(input("enter length of list:"))
for i in range(0, n):
    ele = int(input())
    l.append(ele)
print(ls,end=",")

print("\n")
for i in range (0,len(l)):
    for j in range (I+1,len(l)):
        if l[i]>=l[j]:
            temp = l[i]
            l[i]=l[j]
            l[j]=temp
print(typle(l))

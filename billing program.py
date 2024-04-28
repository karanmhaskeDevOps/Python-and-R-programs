#karan , program for to calculate bill of products

a=int(input("quantity of mango:"))
b=int(input("quantity of apple:"))
c=int(input("quantity of banna:"))
d=int(input("quantity of pinaple:"))
e=int(input("quantity of orange:"))
f=int(input("quantity of badam:"))
g=int(input("quantity of kaju:"))            
h=int(input("quantity of dal:"))
T=(a*200)+(b*40)+(c*70)+(d*50)+(e*78)+(f*90)+(g*90)+(h*100)
print(" mango payment:",(a*200))
print("apple payment :",(b*40))
print("banna payment:",(c*70))
print("pinaple payment:",(d*50))
print("orange payment:",(e*78))
print("badam payment :",(f*90))
print("kaju payment :",(g*90))
print("dal payment:",(h*100))
if T>9500:
    p=T-(T*(12/100))
    print("AFter appling 12% discount ",p)
elif t>6500 and T<9500:
    q=(T*(9/100))
    print("After appling 9% discount",q)
else:
    r=(T*(3/100))
    print("After appling 3% discount, Payment is ",r)

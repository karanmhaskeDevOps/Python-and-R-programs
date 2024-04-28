#karan , program for at and gc content

x=input("enter the sequence:")

countat=0
countgc=0

for i in x:
        if i=='a' or i=='t':
            countat+=1
        else:
            countgc+=1

perat=(countat/len(x))*100
pergc=(countgc/len(x))*100
print("""AT content = {}\nGC content = {}""".format(perat,pergc))

#karan, program for atgc count and there percentag

x=input("enter the seq:")
counta=0
countt=0
countg=0
countc=0

for i in x:
    if i=='a':
        counta+=1
    elif i=='t':
        countt=+1
    elif i=='g':
        countg+=1
    else: 
        countc+=1

pera=(counta/len(x))*100
pert=(countt/len(x))*100
perg=(countg/len(x))*100
perc=(countc/len(x))*100

print("""Total seq length is
\nper of a is {}
\nper of t is {}
\nper of g is {}
\nper of c is {}""".format(len(x),pera,pert,perg,perc))

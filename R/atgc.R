#karan A,T,G,C,AT and GC content


x='AGCTAGCTAGCTAGTGT'
counta=0
countt=0
countg=0
countc=0
for(i in x)
{
if(i=='A'){
counta=counta+1
}
if(i=='T'){
countt=countt+1
}
if(i=='G'){
countg=countg+1
}
if(i=='C'){
countc=countc+1
}
}
print(counta)
print(countt)
print(countg)
print(countc)
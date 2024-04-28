#Hem
#Prime numbers between 1 to 100
x <- c(1:100)
for (i in x){
  if (i==2 | i==3 | i==5 | i==7){
    cat(i,"\t")
  }else if(i%%2!=0 & i%%3!=0 & i%%5!=0 & i%%7!=0){
    cat(i,"\t")
  }
}
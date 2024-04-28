#Hem
#A,T,G,C,AT and GC content
x <- readline(prompt = "Enter sequence: ")
y <- strsplit(x, "")[[1]]
counta=0
countt=0
countg=0
countc=0
for(i in y)
{
  if(i=='A'){
    counta=counta+1
  }else if(i=='T'){
    countt=countt+1
  }else if(i=='G'){
    countg=countg+1
  }else{
    countc=countc+1
  }
}
pera <- (counta/nchar(x))*100
pert <- (countt/nchar(x))*100
perg <- (countg/nchar(x))*100
perc <- (countc/nchar(x))*100
cat("\nPercentage of A is ",pera)
cat("\nPercentage of T is ",pert)
cat("\nPercentage of G is ",perg)
cat("\nPercentage of C is ",perc)
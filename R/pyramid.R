#karan Pyramid of

x=c()
for (i in 1:5) {
  for (j in 1:i+1) {
    x = c(x,'*')
  }
  print(x)
  x=c()
}


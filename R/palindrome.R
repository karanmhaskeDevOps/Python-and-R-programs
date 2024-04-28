#karan Palindrome or not

x <- readline(prompt = "Enter sequence: ")
y <- strsplit(x, "")[[1]]
z <- ""
for (i in y){
  z=paste(i,z,sep = "")
}

if (identical(x,z)){
  print("Palindrome")
}else{
  print("Not a palindrome")
}


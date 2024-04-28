#karan, palindrom or not

def pal(x):
    y=""
    for i in x:
        y=i+y

    if x == y:
        print("palindrome")
    else:
        print("not a palindrom")

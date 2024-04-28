#karan, program for tuple

#creating a tuple
t1=('c','c++','java','python')
print(t1)
print(len(t1))

#type of data
print(type(t1))

#typle slicing
print(t1[0])
print(t1[1:])
print(t1[::-1])
print(t1[2:4])

#tuple concatenation
t2 = (1,2,3,4,5)
t3 = (True,False,True)
print(t1+t2+t3)

#List to typle
l=[6,7,8,9,0]
print(tuple(l))

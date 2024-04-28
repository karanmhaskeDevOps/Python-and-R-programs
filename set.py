#KARAN , Pogram for set

s1 = {11,12,13}
print(s1)
s2 = {19,"python",(1,9,6)}
print(s2)
s3 = set([11,12,13])
print(s3)

#type of data
print(type(s3))

#initializing sets
s1.add(50)
print(s1)
s1.update([65,95,100])

#adding list and set
s1.update([110,120],{1,6,8})
print(s1)

#removing elementes
s1.discard(12)
print(s1)
s1.remove(13)
print(s1)

#String as set
setstr = set("hello Pyhton")
print(setstr)
print(setstr.pop())
print(setstr.clear())

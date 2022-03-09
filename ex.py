# for i in range (5):
#     print(" "*(5-i)+"*"*(i+1)+"*"*(i))

# a = 0
# while a < 10:
#    a = a + 1
#    if a % 2 == 1: continue
#    print(a)


# for i in range(2,10):
#   for b in range(1,10):
#     print("%d*%d=%d"%(i,b,(i*b)))

# for i in range(2,10):
#     for j in range(1,10):
#         print("{}*{}={}".format(i,j,i*j))



# a=0
# sum=0
# while a<1000: 
#   a+=1
#   if a%3==0:
#     sum+=a
# print(sum)
# a=0
# while a<5:
#   a+=1
#   print("*"*a)

# for i in range (1,101):
#     print (i)

# lst=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# sum=0
# for i in range (len(lst)):
#   sum+=lst[i]
# average=sum/len(lst)
# print(average)
  

# def add(a, b): 
#     return a + b

# a = add(1, 2)
# print(a)
# print(add(3, 6))
# print()
# add()

import tensorflow as tf
print(tf.__version__)
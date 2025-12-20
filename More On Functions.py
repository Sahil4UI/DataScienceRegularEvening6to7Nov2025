# paise = [10000,20000,5000,9000,560000,75400]
# def rupee(a):
#     return a/100
# res = list(map(rupee,paise))
# print(res)

# paise = [10000,20000,5000,9000,560000,75400]
# res = list(map(lambda x:x/100,paise))
# print(res)

# rslt= []
# for value in paise:
#     rslt.append(rupee(value))
# print(rslt)
# store all even numbers in a list

# x = [1,2,3,4,5,6,7,8,9,10]
# res = []

# def Even(a):
#     if a%2==0:
#         return True
#     else:
#         return False

# for i in x:
#     if(Even(i)==True):
#         res.append(i)
# print(res)

# def Even(a):
#     if a%2==0:
#         return True
#     else:
#         return False

# x = [1,2,3,4,5,6,7,8,9,10]

# Even = lambda a : True if a%2==0 else False
# res = list(filter(Even,x))
# print(res)

# list comprehension
from functools import reduce
a = [i for i in range(1,11)]
print(reduce(lambda x,y:x*y , a))

# 1.find sum of all elements of list
# x = [1,2,3,5,30,23,34,5,-10]
# print(sum(x))

# 2.Multiply all elements of list
# x = [1,2,3,5,30,23,34,5,-10]
# result = 1
# for num in x:
#     result *= num
# print(result)

# 3.find largest and smallest from list
# 5.
# x = ['abc', 'xyz', 'aba', '1221','101']
# count = 0
# for string in x:
#     if string[0]==string[-1]:
#         count+=1
# print(count)

# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
# x = [1,1,2,2,2,2,2,3,3,3,4,4,4,5,5,5]
# print(list(set(x)))

# result = []
# for num in x:
#     if num not in result:
#         result.append(num)
# print(result)

# check if list is empty or not
# x = [1]
# print("Empty" if len(x)==0 else "Not Empty")

# Clone or Copy a List
# x = [1,2,3,4,5]
# y = x.copy()
# from copy import deepcopy
# x = [1,2,3,[4,5]]
# y = deepcopy(x)
# print(y)

x = ["hello","welcome","to","Samyak"]
n = 5
for string in x:
    if len(string)>n:
        print(string)


# https://www.w3resource.com/python-exercises/list/

Python 3.14.0 (v3.14.0:ebf955df7a8, Oct  7 2025, 08:20:14) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #List  - List is pythons ordered and mutable data collection
>>> x = [1,2,3,4,5,6,6]
>>> type(x)
<class 'list'>
>>> #ordered = indexing
>>> x[0]
1
>>> x[1]
2
>>> x[3]
4
>>> x[-1]
6
>>> #slicing
>>> x
[1, 2, 3, 4, 5, 6, 6]
>>> x[0:4]
[1, 2, 3, 4]
>>> x[::-1]
[6, 6, 5, 4, 3, 2, 1]
>>> x = [1,2,3,4,5,6,[7,8,9,[10,11,12]]]
>>> x[6][3][1]
11
>>> #mutable
x = [1,2,3]
x.append(200)
#it will append the value at the end of the list
x
[1, 2, 3, 200]
x.append(100)
x
[1, 2, 3, 200, 100]
x.insert(0,230)
x
[230, 1, 2, 3, 200, 100]
x.pop()#it will remove the last value
100
x
[230, 1, 2, 3, 200]
x.pop()
200
x
[230, 1, 2, 3]
del x[3]
x
[230, 1, 2]
x.remove(230)
x
[1, 2]
x.clear()
x
[]
#list comprehension
x = [i for i in range(1,11)]
x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum(x)
55
max(x)
10
min(x)
1
x = [10,20,30,1,-10,0]
x.sort()
x
[-10, 0, 1, 10, 20, 30]
x.sort(reverse=True)
x
[30, 20, 10, 1, 0, -10]
x = [1,2,3,4]
y = [5,6,7,8]
x+y
[1, 2, 3, 4, 5, 6, 7, 8]
x*y
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    x*y
TypeError: can't multiply sequence by non-int of type 'list'
x.extend(y)
x
[1, 2, 3, 4, 5, 6, 7, 8]
x.clear()
del x
x
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    x
NameError: name 'x' is not defined
x = [10,100,1000,0,-10,20,40,1,1,1,1]
x.count(1)
4
x.find(10)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    x.find(10)
AttributeError: 'list' object has no attribute 'find'
x.index(10)
0
x.index(100)
1
x
[10, 100, 1000, 0, -10, 20, 40, 1, 1, 1, 1]
x = [1,2,3,4]
x
[1, 2, 3, 4]
x*3
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
#deep copy vs shallow copy
x = [1,2,3,4]
y = x
id(x)
4457401856
id(y)
4457401856
x
[1, 2, 3, 4]
x.pop()
4
x
x
[1, 2, 3]
y
[1, 2, 3]
x
[1, 2, 3]
y = x.copy()
x
[1, 2, 3]
y
[1, 2, 3]
x.pop()
3
x
[1, 2]
y
[1, 2, 3]
#shallow copy
x = [1,2,3,4,[5,6,7]]
y = x.copy()
del x[0]
x
[2, 3, 4, [5, 6, 7]]
y
[1, 2, 3, 4, [5, 6, 7]]
del y[-1][0]
y
[1, 2, 3, 4, [6, 7]]
x
[2, 3, 4, [6, 7]]
from copy import deepcopy
x
[2, 3, 4, [6, 7]]
y = deepcopy(x)
x
[2, 3, 4, [6, 7]]
y
[2, 3, 4, [6, 7]]
del x[-1][0]
x
[2, 3, 4, [7]]
y
[2, 3, 4, [6, 7]]
x = [10,20,30,40,50]
for item in x:
    print(item)

10
20
30
40
50

for i in range(len(x)):
    print(x[i])

10
20
30
40
50

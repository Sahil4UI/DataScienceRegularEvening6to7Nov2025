Python 3.14.0 (v3.14.0:ebf955df7a8, Oct  7 2025, 08:20:14) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
#Tuple- tuple is python's immutable and ordered data collection
#immutable - cannot edit
x = (1,2,3,4,5)
type(x)
<class 'tuple'>
x.append()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    x.append()
AttributeError: 'tuple' object has no attribute 'append'
x.append(90)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x.append(90)
AttributeError: 'tuple' object has no attribute 'append'
x
(1, 2, 3, 4, 5)
del x[0]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
x[0]
1
x[-1]
5
x[0:4]
(1, 2, 3, 4)
x
(1, 2, 3, 4, 5)
x = (1,1,1,2,2,2,2,3,3,3,3,3,3)
len(x)
13
x.count(2)
4
x.index(2)
3
x = (1)
type(x)
<class 'int'>
x = (1,)
type(x)
<class 'tuple'>
#SET
#set is pythons unordered and mutable data collection
x = {1,2,3,4,5}
type(x)
<class 'set'>
#set cannot store duplicates
x.add(1)
x
{1, 2, 3, 4, 5}
x = {1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4}
x
{1, 2, 3, 4}
y = {3,4,5,6}
>>> x
{1, 2, 3, 4}
>>> y
{3, 4, 5, 6}
>>> #union - all but without repetition
>>> x.union(y)
{1, 2, 3, 4, 5, 6}
>>> #intersection - common
>>> x.intersection(y)
{3, 4}
>>> x
{1, 2, 3, 4}
>>> y
>>> x.difference(y)
{1, 2}
>>> y.difference(x)
{5, 6}
>>> x
{1, 2, 3, 4}
>>> y = {1,2}
>>> x.issubset(y)
False
>>> x.issuperset(y)
True
>>> y.issubset(x)
True

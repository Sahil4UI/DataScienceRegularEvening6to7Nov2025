Python 3.14.0 (v3.14.0:ebf955df7a8, Oct  7 2025, 08:20:14) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #Dictionary:
>>> #word(key):meaning(value)
>>> #key:value pair enclosed inside a {} brackets separated by commas (,) is dictionary
>>> x = {"id":101,"name":"ram","age":18,"class":12}
>>> type(x)
<class 'dict'>
>>> #dictionary is unordered
>>> #no indexing
>>> x["id"]
101
>>> x.get("id")
101
>>> x.get("name")
'ram'
>>> #inserting contact no
>>> x["contact"]=9876543210
>>> x
{'id': 101, 'name': 'ram', 'age': 18, 'class': 12, 'contact': 9876543210}
>>> #dictionary
>>> #cannot have duplicate keys
>>> x
{'id': 101, 'name': 'ram', 'age': 18, 'class': 12, 'contact': 9876543210}
>>> x["id"]=102#updating the value
>>> x
{'id': 102, 'name': 'ram', 'age': 18, 'class': 12, 'contact': 9876543210}
>>> x.pop("contact")
9876543210
>>> x
{'id': 102, 'name': 'ram', 'age': 18, 'class': 12}
>>> x.popitem()#it will remove last key value pair
('class', 12)
x
{'id': 102, 'name': 'ram', 'age': 18}
del x["id"]
x
{'name': 'ram', 'age': 18}
x.clear()
x
{}
x = {'id': 101, 'name': 'ram', 'age': 18, 'class': 12, 'contact': 9876543210}
for key in x:
    print(key)

id
name
age
class
contact
x.keys()
dict_keys(['id', 'name', 'age', 'class', 'contact'])
x.values()
dict_values([101, 'ram', 18, 12, 9876543210])
x.items()
dict_items([('id', 101), ('name', 'ram'), ('age', 18), ('class', 12), ('contact', 9876543210)])
len(x)#how many key value pairs are there
5
for key in x:
    print(key,"\t",x[key])#\t -escape sequence

id 	 101
name 	 ram
age 	 18
class 	 12
contact 	 9876543210
#list - list is pythons ordered data typed
x = [1,2,3,4,5]
type(x)
<class 'list'>
data = [{"id":101,"name":"ram","age":18,"class":12},]
data = [{"id":101,"name":"ram","age":18,"class":12},{"id":101,"name":"ram","age":18,"class":12}]
data = [{"id":101,"name":"ram","age":18,"class":12},{"id":102,"name":"AMIT","age":18,"class":12}]
data
[{'id': 101, 'name': 'ram', 'age': 18, 'class': 12}, {'id': 102, 'name': 'AMIT', 'age': 18, 'class': 12}]
for row in data:
    for key in row:
        print(key,"\t",rows[key])

Traceback (most recent call last):
  File "<pyshell#46>", line 3, in <module>
    print(key,"\t",rows[key])
NameError: name 'rows' is not defined. Did you mean: 'row'?
for row in data:
    for key in row:
        print(key,"\t",row[key])

id 	 101
name 	 ram
age 	 18
class 	 12
id 	 102
name 	 AMIT
age 	 18
class 	 12

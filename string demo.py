Python 3.14.0 (v3.14.0:ebf955df7a8, Oct  7 2025, 08:20:14) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #String : "String is python's immutable and ordered data type
>>> #immutable : which cannot be changed or modified....
>>> #ordered : indexing
>>> x = "hello Welcome to String"
>>> type(x)
<class 'str'>
>>> len(x)
23
>>> x.upper()
'HELLO WELCOME TO STRING'
>>> x.lower()
'hello welcome to string'
>>> x.capitalize()
'Hello welcome to string'
>>> x.title()
'Hello Welcome To String'
>>> x.swapcase()
'HELLO wELCOME TO sTRING'
>>> x
'hello Welcome to String'
>>> x.replace("String","Python")
'hello Welcome to Python'
>>> x
'hello Welcome to String'
>>> x = x.replace("String","Python")
>>> x
'hello Welcome to Python'
>>> x.count("o")
4
#indexing
x
'hello Welcome to Python'
x[0]
'h'
x[-1]
'n'
\
x[-1]
'n'
x[-2]
'o'
#slicing
x
'hello Welcome to Python'
#x[starting:ending:stepsize]
x[0:6]#here ending is n-1
'hello '
x[0:]
'hello Welcome to Python'
x[:11]
'hello Welco'
x[:]
'hello Welcome to Python'
x[::2]
'hloWloet yhn'
x[::-1]#$reverse
'nohtyP ot emocleW olleh'
x
'hello Welcome to Python'
x.find("o")#first occurence
4
x.rfind("o")#last occurence
21
x.find("o",5)
10
x.index("o",5)
10
x.find("X")#-1 means value not find
-1
x.index("X")
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    x.index("X")
ValueError: substring not found
x
'hello Welcome to Python'
x.isupper()
False
x.islower()
False
x = "werfsedf"
x.isalpha()
True
x = "fgedrt54"
x.isalpha()
False
x.isalnum()
True
x
'fgedrt54'
x = "string is immutable"
x*3
'string is immutablestring is immutablestring is immutable'
x = "hey"
y = "python"
x+y
'heypython'
x = "python is a hugh level programming language"
a = x.split()
a
['python', 'is', 'a', 'hugh', 'level', 'programming', 'language']
a[0]
'python'
a[-1]
'language'
a
['python', 'is', 'a', 'hugh', 'level', 'programming', 'language']
a.join(" ")
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a.join(" ")
AttributeError: 'list' object has no attribute 'join'
" ".join(a)
'python is a hugh level programming language'
"#".join(a)
'python#is#a#hugh#level#programming#language'

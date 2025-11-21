#Write a program to check whether a given number is even or odd
'''
x = int(input("Enter No:"))

if x%2==0:
    print("Ev
    en")
else:
    print("Odd")
'''
#multi line comment

#Write a program to find the largest b/w 2 numbers
'''
x = int(input("Enter No1:"))
y = int(input("Enter No2:"))

if x>y:
    print(x,"is largest")
elif x==y:
    print("both are equal")
else:
    print(y,"is largest")
'''
#Write a program to find the largest b/w 3 numbers
x = int(input("Enter No1:"))
y = int(input("Enter No2:"))
z = int(input("Enter No3:"))

if x>y and x>z:
    print(x,"is largest")
elif y>z:
    print(y,"is largest")
else:
    print(z,"is largest")

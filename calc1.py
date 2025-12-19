def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

# user input
x = int(input("Enter No1:"))
y = int(input("Enter No2:"))
choice = input("Enter +,-,/,* :")
d = {"+":sum,"-":sub,"/":div,"*":mul}
result = d.get(choice)(x,y)
# DRY  - Dont Repeat Yourself
print(result)
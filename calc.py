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
result = None
if choice == "+":
    result=sum(x,y)
elif choice == "-":
    result = sub(x,y)
elif choice == "*":
    result = mul(x,y)
elif choice == "div":
    result = div(x,y)
# DRY  - Dont Repeat Yourself

print(result)
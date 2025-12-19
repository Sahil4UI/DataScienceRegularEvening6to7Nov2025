# def calculator(a,opr,b):
#     # evaluate
#     return eval(a+opr+b)

# lambda function
calculator = lambda a,opr,b : eval(a+opr+b)
# user input
x,y,choice = input("Enter No1:"),input("Enter No2:"),input("Enter +,-,/,* :")
print(calculator(x,choice,y))
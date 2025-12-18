#function - create once and use multiple times.
#function definition
# def f1():
#     print("F1 Called")
# function calling
# f1()
# arguments and parameter
# x,y - parameter
# def f1(x,y):
#     print(x+y)

# arguments -12,13
# f1(12,13)

# optional paramter
# def f1(x,y=20):
#     print(x+y)

# f1(10,5)
# *y - n paramter
# def f1(x,*y):
#     print(x,y)

# f1(1,2,3,4,5,6,7)
# ** keyworded arguments
# def f1(roll,name,**other):
#     print(roll,name,other)

# f1(101,"ravi",div = "10th",contact = "9876543210")

# function with return value
# def f1(x,y):
#     return x+y

# result=f1(12,3)
# print(result)

# nested function
# def f1():
#     # local scope
#     def f2():
#         print("Function 2 Called....")
#     def f3():
#         print("Function 3 Called....")

#     return f2,f3

# f2 = f1()[0]
# f2()
# f3 = f1()[1]
# f3()


# recursive function
# when a function calls itself again and again that function
#  is called recursive function

def f1(x):
    if x>10:
        return
    print(x)
    f1(x+1)

f1(1)












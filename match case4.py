x = int(input("Enter X Coordinates : "))
y = int(input("Enter Y Coordinates : "))

match (x,y):
    case (0,0):
        print("Origin")
    case _ :
        print("Not on Origin")
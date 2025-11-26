# python 3.10 + - match case
order = input("Type Start to Start the System")

match order:
    case "Start":print("System Started...")
    case _ :print("invalid command")

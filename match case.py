# python 3.10 + - match case
order = int(input('''
                 Press 1 to Order Pizza
                 Press 2 to order Burger
                 Press 3 to Order Cold Drink : '''))

match order:
    case 1:print("Pizza Ordered Successfully....")
    case 2:print("Burger Ordered Successfully...")
    case 3:print("Cold Drink Ordered Successfully")
    case _ :print("Out of Stock")

#difine the menu of restaurant
menu = {
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80,
    'Maggi':50,
    'Black Coffee':150,
    'Fried Rice':60,
}
#Greeet
print("Welcome to PYTHON Restaurant")
print("pizza: Rs40\npasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs80\nMaggi: Rs50\nBlack Coffee: Rs150\nFried Rice: Rs60")

order_total = 0
#80 + 50 =130 like this

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1] #0 + 40
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"0order item {item_1} is not available yet!")
    
another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"0orderd item {item_2} is not avaiable!")

    print(f"The total amount of items to pay is {order_total}")
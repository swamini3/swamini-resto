#Define the menu of restaurant 
menu = {
    'Pizza':110,
    'Pasta':70,
    'Salad':50,
    'Burger':90,
    'Coffee':80,
    'French fries':120,
}
print(menu)

#Greet
print(" Welcome to SWAMINI Restaurant")
print(" Pizza :RS110\n Pasta :RS70\n Salad :RS50\n Burger :RS90\n Coffee :RS80\n French Fries :RS120\n")

order_total = 0 
#80+70 = 150
item_1= input("Enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet")

another_order = input("Do you want to add another item? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print("Item {item_2}has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")

    print(f"The total amount of items is to pay is {order_total}")




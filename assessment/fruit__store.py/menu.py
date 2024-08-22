fruit_stock={}
def add_fruit():
    f=open("fruit.txt","a")
    print("\nADD FRUIT STOCK")
    fruit = input("Enter Fruit Name: ").capitalize()
    qty = int(input(f"Enter quantity for {fruit} (in kg): "))
    price = int(input(f"Enter price per kg for {fruit}: "))

    if fruit in fruit_stock:
        fruit_stock[fruit]['qty'] += qty
        fruit_stock[fruit]['price'] = price
    else:
        fruit_stock[fruit] = {'qty': qty, 'price': price}
    
    print(f"{fruit} stock updated successfully!")

def view_fruit():
    print("\nVIEW FRUIT STOCK")
    if fruit_stock:
        for fruit, details in fruit_stock.items():
            print(f"{fruit} - Quantity: {details['qty']} kg, Price: {details['price']} INR/kg")
    else:
        print("No fruits available in stock.")

def update_fruit():
    print("\nUPDATE FRUIT STOCK")
    fruit = input("Enter the fruit name to update: ").capitalize()
    if fruit in fruit_stock:
        new_qty = int(input(f"Enter the new quantity for {fruit} (in kg): "))
        new_price = int(input(f"Enter the new price per kg for {fruit}: "))
        fruit_stock[fruit] = {'qty': new_qty, 'price': new_price}
        print(f"{fruit} stock updated successfully!")
    else:
        print(f"{fruit} not found in stock.")
# Global dictionary to store fruit stock
fruit_stock = {}

def manager():
    while True:
        print("\nFruit Market Manager Menu")
        print("1) Add Fruit Stock")
        print("2) View Fruit Stock")
        print("3) Update Fruit Stock")
        print("4) Go Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_fruit()
        elif choice == '2':
            view_fruit()
        elif choice == '3':
            update_fruit()
        elif choice == '4':
            break  # Exit the manager menu and go back to the main menu
        else:
            print("Invalid choice, please select a valid option.")

def customer():
    while True:
        print("\nCustomer Menu")
        print("1) View Available Fruits")
        print("2) Go Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_fruit()
        elif choice == '2':
            break  # Exit the customer menu and go back to the main menu
        else:
            print("Invalid choice, please select a valid option.")

def add_fruit():
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

# Main Program
print("WELCOME TO FRUIT MARKET")
while True:
    print("\nSelect your Role:")
    print("1) Manager")
    print("2) Customer")
    print("3) Exit")
    role_choice = input("Enter your choice: ")

    if role_choice == '1':
        manager()
    elif role_choice == '2':
        customer()
    elif role_choice == '3':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice, please select a valid option.")

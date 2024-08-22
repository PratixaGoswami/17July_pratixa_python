from menu import view_fruit
def customer():
    while True:
        print("\nCustomer Menu")
        print("1) View Available Fruits")
        print("2) Go Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_fruit()
        elif choice == '2':
            break  
        else:
            print("Invalid choice, please select a valid option.")
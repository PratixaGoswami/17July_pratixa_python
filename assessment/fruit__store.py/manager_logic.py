from menu import add_fruit, view_fruit ,update_fruit 

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
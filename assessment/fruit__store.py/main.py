from manager_logic import manager
from customer_logic import customer
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

import business_logic


class admin:
        def register(self):
            self.a_username=input("Enter  admin username:")
            self.a_password=input("Enter password:")
            print("admin register sucessfully")
            
        def login(self):
            self.a_username=input("Enter admin username:")
            self.a_password=input("Enter password:")
class manager(admin):
        def  register(self):
            name=input("Enter your name:") 
            pharmacy_name=input("Enter your pharmacy name:") 
            username=input("Enter username:")
            m_password=input("Enter password:") 
            business_logic.m_logic.insertdata(name,pharmacy_name,username,m_password)
        
          
        def login(self):
              return super().login()           

             

m=manager()
while True:
    print("")
    print("\nSelect your Role:")
    print("1) Admin")
    print("2) Pharmacy manager")
    print("3)  EXIT")
    role_choice=input("Enter your role choice:")

    if role_choice=='1':
            while True:
                print("1) register")
                print("2) login")
                print("3) view all manager")
                print("4)view all medicine")
                print("5) Exit")
                role_choice=input("enter your role choice:")
                if role_choice=="1":
                      m.register()
                elif role_choice=='2':
                      m.login()  
                elif role_choice=='3':
                      business_logic.m_logic.showdata()
                elif role_choice=='4':
                      business_logic.m_logic.view_medicine()
                elif role_choice=='5':
                      break
                else:
                      print("Invalid choice please select valid option")         
                      
                                
          

    elif role_choice == '2':
            while True:
                print("1) register")
                print("2) login")
                print("3) Add medicine")
                print("4) view medicine")
                print("5) Delete medicine")
                print("6) Exit")
                role_choice=input("Enter your role choice:")
                if role_choice=='1':
                      m.register()
                elif role_choice=='2':
                      m.login()   
                elif role_choice=='3':
                      medicine_name=input("Enter medicine name:")
                      qty=input("enter quantity of medicine:")
                      price=input("Enter price of medicine:")
                      business_logic.m_logic.insert_medicine(medicine_name,qty,price)
                elif role_choice=='4':
                      business_logic.m_logic.view_medicine()
                elif role_choice=='5':
                      id=input("enter id of medicine:")
                      business_logic.m_logic.delete_medicine(id)
                elif role_choice=="6":
                      break
                else:
                      print("Invalid choice please select valid option") 


    elif role_choice == '3':
            print("Exiting the program")
            break
    else:
            print("Invalid choice, please select a valid option.") 

# 





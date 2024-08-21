balance=0
def account_opening():
    a_number=int(input("Enter Acount number:"))
    a_type=input("Enter Account type (saving /current):")
    h_name=input("Enter Holder name:")
    return a_number,a_type,h_name

def deposite():
        global balance
        while True:
                d_amount=int(input("Enter deposite amount min 2000:"))
                if(d_amount<2000):
                        print("Error: Minimum deposit amount is 2000.")
               

                else:       
        
                        balance += d_amount
                        print("Balance is:",balance) 
                        return balance
def withdrawal():
        global balance
        w_amount=int(input("Enter Withdrawal Amount:"))
        if w_amount>balance:
            print("Error: Insufficient balance.")
        else:  

                balance-= w_amount
                print("Balance is:",balance) 
                return balance
                
x=account_opening()
b=deposite()
b=withdrawal()
print(" ")
print("Account number is:",x[0])
print("Acount type:",x[1])
print("Account holder name:",x[2])
print("Total balance:",balance)
 
           
              

        



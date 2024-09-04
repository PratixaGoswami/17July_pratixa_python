import random

class account_opening:
    a_number=0
    a_type=""
    h_name=""
    def a_getdata(self):
        self.a_number=random.randint(111111,999999)
        self.a_type=input("Enter Account type (saving /current):")
        self.h_name=input("Enter Holder name:")

class deposite():
    
    balance=0
    
    def d_getdata(self):
        while True:
                d_amount=int(input("Enter deposite amount min 2000:"))
                if(d_amount<2000):
                        print("Error: Minimum deposit amount is 2000.")
                

                else:       
            
                    self.balance += d_amount
                    print("Balance is:",self.balance) 
                    break

class withdrawal(deposite): 
     
   w_amount=0
   def w_getdata(self): 
        while True:   
                    w_amount=int(input("Enter Withdrawal Amount:"))
                    if w_amount>self.balance:
                            print("Error: Insufficient balance.")
                    else:  

                        self.balance-= w_amount
                        print("Balance is:",self.balance) 
                        break

class printdata(withdrawal,account_opening):

    def prindata(self):
        print("Account number is:",self.a_number)
        print("Acount type:",self.a_type)
        print("Account holder name:",self.h_name)
        print("Total balance:",self.balance)                
bank=printdata()
bank.a_getdata()
bank.d_getdata()
bank.w_getdata()
bank.prindata()


             
                        


               
                                        
                       

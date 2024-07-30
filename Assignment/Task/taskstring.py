
name=input("Enter Your Name:")

if  name.isalpha():
    print("done")   

    age=input("Enter your age:")

    if age.isdigit():
        print("done")  
        email=input("Enter your email:")  

        if email.casefold():
              print("done")
    
              num=input("Enter your mobile number:") 
              if len(num)==10 and num.isdigit():
                print("Done")
              else:
                  print("enter a valid 10-digit mobile number") 
        else:
            print("enter only small letter")
    else:
       print("enter only number")
else:
    print("enter only letter for the name")

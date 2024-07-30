n=int(input("Enter a positive number:"))
if n <=0 :
    print("Error")
else:
    total=0
    for i in range (1,n+1):
        total +=i
    print("the  sum of the first ",n,":Positive  integers is:",total)
    
   

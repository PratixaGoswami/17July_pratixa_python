x=open("table.txt","a")

n=int(input("How many store table in file:"))
for i in range(n):
        table_num=int(input("enter table number:"))
        for j in range(1,11):
            x.write(f"{table_num}*{j}={table_num * j}\n")
        
        
    
    
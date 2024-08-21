'''def getdata():
    id=int(input("Enter your id:"))
    name=input("Enter your name:")
    city=input("Enter your city:")
    print(id) 
    print(name)
    print(city)
    print(" ")

n=int(input(" enter Number of student:"))
for i in range(n):
    getdata()'''

def stdata(id,name,city):
    print("id:",id)
    print("name:",name)
    print("City:",city)
n=int(input(" Enter Number of student:"))
for i in range(n):
    stid=input("Enter your id:")
    stname=input("Enter your name:")
    stcity=input("Enter your city:")   
    stdata(stid,stname,stcity)


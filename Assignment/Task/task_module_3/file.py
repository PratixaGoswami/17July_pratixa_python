x=open("studentdata.txt","a")
student=int(input("enter number of student:"))
for i in range(student):
    id=input("Enter your id:")
    x.write(f"id:{id}\n")
    name=input("Entetr your name:")
    x.write(f"name:{name}\n")
    city=input("Enter your city:")
    x.write(f"city:{city}\n")



import pymysql

try:
    dbcon=pymysql.connect(host='localhost',user='root',password='root',database="pydatabse")
    print("database connected!")
except Exception as e:
    print(e)

cr=dbcon.cursor()

tbl_create="create table pystud(id integer primary key auto_increment,name varchar(20),city varchar(20))"
try:
    cr.execute(tbl_create)
    print("table created")
except Exception as e:
    print(e) 


s_name=input("Enter your name:") 
s_city=input("enter your city:")   
insert_value=f"insert into pystud(name,city)values('{s_name}','{s_city}')"
try:
    cr.execute(insert_value)
    dbcon.commit()
    print("values inserted")
except Exception as e:
    print(e)    







show_data="select*from pystud"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    for i in data:
        print(i)
except Exception as e:
    print(e) 

       
stud_id=int(input("enter id:"))

del_data=f"delete from pystud where id = {stud_id}"  
try:
    cr.execute(del_data)
    dbcon.commit()
    print("record are deleted!")

except Exception as e:
    print(e)    


s_id=int(input("enter the id of student to update:"))
s_name=(input("Enter name of student to upadte:"))
s_city=(input("enter city of student to update:"))


update_data=f"update pystud set name='{s_name}',city='{s_city}' where id= {s_id}"
try:
    cr.execute(update_data)
    dbcon.commit()
    print("record updated!")
except Exception as e:
    print(e)    

     



















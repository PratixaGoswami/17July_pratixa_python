import pymysql

try:
            
            dbcon=pymysql.connect(host="localhost",user="root",password="root",database="pydatabase")
            print("database connected")
           
   
except Exception as e:
            print(e)

cr=dbcon.cursor()
     
manager="create table manager(SR_No integer primary key auto_increment ,Manger_Name varchar(45),Pharmacy_Name varchar(100),username varchar(45),password integer)"
try:
            cr.execute(manager)
            dbcon.commit()
            
            print("table created")
except Exception as e:
            print(e)


madicine="create table medicine(Sr_no integer primary key auto_increment,medicine_name varchar(100),Qty integer,Added_date date,Added_by integer,price integer,foreign key(Added_by)references manager(SR_No))"
try:
            cr.execute(madicine)
            dbcon.commit()
            print("table created")
except Exception as e:
            print(e)   
          


class manager:  



      
      def insertdata(self,m_username,pharmacy_name,username,password):
            
            
                  insert_data=f"insert into manager(Manger_Name,Pharmacy_Name,username,password)values('{m_username}','{pharmacy_name}','{username}',{password})"   
                  try:
                        cr.execute(insert_data) 
                        dbcon.commit()
                        print(f"manager {m_username} register successfully ")   
                  except Exception as e:
            
                        print(e) 
      def  showdata(self):
                  
                  show_data=f"select*from manager"  
                  try:
                        cr.execute(show_data)
                        data=cr.fetchall()
                  
                        for i in data:
                              print(i)
                            
                  except Exception as e:
                        print(e) 
                        
                      
class medicine(manager):

      def insert_medicine(self,medicine_name,medicine_qty,medicine_price):
                  insert_medicine=f"insert into medicine(medicine_name,Qty,price)values('{medicine_name}','{medicine_qty}',{medicine_price})"
                  try:
                        cr.execute(insert_medicine)  
                        dbcon.commit()
                        print("medicine record are inserted")
                  except Exception as e:
                        print(e)

      def view_medicine(self):
            
                  view_medicine="select*from medicine"

                  try:
                        cr.execute(view_medicine)
                        data=cr.fetchall()
                  
                        for i in data:
                              print(i)
                  except Exception as e:
                        print(e)  

      def delete_medicine(self,medicine_id):

                  del_medicine=f"delete from medicine where Sr_no='{medicine_id}'"

                  try:
                        cr.execute(del_medicine)
                        dbcon.commit()
                        print("record delted")
                  except Exception as e:
                        print(e)

m_logic=medicine()


                                             


      
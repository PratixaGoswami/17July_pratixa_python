import sqlite3
try:
    db=sqlite3.connect("mydb.db")
    print("database connected")
except Exception as e:
    print (e)

create_tbl="create table student(id integer primary key autoincrement,name text,city text,subject text,mobile integer unique)"
try:
     db.execute(create_tbl)
     print("table created")
except Exception as e:
    print(e)

# insert_tbl="insert into student(name,city,subject,mobile)values('pratixa','Amreli','python',9747439759),('Bansi','rajkot','python',9737409700),('bhumi','rajkot','python',8738419749)" 
# try:
#      db.execute(insert_tbl)
#      db.commit()
#      print("record inserted")
# except Exception as e:
#     print(e)  

update_tbl="update student set name='radhika',city='surat' where id=3"
try:
     db.execute(update_tbl)
     db.commit()
     print("table updated!")
except Exception as e:
    print(e)

delete_data="delete from student where id=8"
try:
     db.execute(delete_data)
     db.commit()
     print("record deleted!")
except Exception as e:
    print(e)

cr=db.cursor()
show_data="select*from student"
try:
    cr.execute(show_data)
    # data=cr.fetchall()
    data=cr.fetchmany(3)
    # data=cr.fetchone()

    for i in data:
        print(i)
except Exception as e:
    print(e)        




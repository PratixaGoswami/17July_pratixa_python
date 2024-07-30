maths=int(input("Enter marks of maths:"))
eng=int(input("Enter marks of eng:"))
hindi=int(input("Enter marks of hindi:"))
gujrati=int(input("Enter marks of gujrati:"))
total=maths+eng+hindi+gujrati
per=total/4
print("total", total)
print("per",per)

if maths>33 and eng>33 and hindi>33 and gujrati>33:

  if per>80:
    print("first class")
  elif  per>60:   
    print("Second class")
  elif per>40:
    print("pass")
 
  else:
    print("fail")
else:
  print("fail")    













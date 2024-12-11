from django.shortcuts import render,redirect
from .forms import*
from django.contrib.auth import logout
from .crud import create_object, read_objects, update_object, delete_object
# Create your views here.
def index(request):
    user=request.session.get('user')
    return render(request,'index.html',{'user':user})

def signup(request):
    msg=""
    if request.method=="POST":
        newreq=signupForm(request.POST)
        if newreq.is_valid:
            newreq.save()
            print("signup successfully")
            msg="Signup Successfully!"
        else:
            (newreq.errors)
            msg="Error... Something went Wrong"    

    return render(request,'signup.html',{'msg':msg})

def login(request):
    msg=""
    if request.method=="POST":
        unm=request.POST['username']
        pas=request.POST['password']
        loginuser=signupmodel.objects.filter(username=unm,password=pas)

        if loginuser:
            
            print("Login successfully")
            request.session['user']=unm
            return redirect("/")
        else:
            print('Error...Something went wrong')
            msg="Error...Something went wrong"
    return render(request,'login.html',{'msg':msg})

def userlogout(request):
        logout(request)
        return redirect('login')
#student
def students(request):
    return read_objects(request, model=add_student, template_name='students.html')
def ad_student(request):
    return create_object(request, model=add_student, template_name='add_student.html', success_url='/students/')

def update_students(request, id):
    return update_object(request, model=add_student, template_name='update_students.html', success_url='/students/', id=id)

def delete_student(request, id):
    return delete_object(request,model=add_student,success_url='/students/',id=id )
#teacher
def teachers(request):
    return read_objects(request, model=teacher, template_name='teachers.html')

def add_teacher(request):
    return create_object(request, model=teacher, template_name='add_teacher.html', success_url='/teachers/')
def update_teacher(request,id):
    return update_object(request, model=teacher, template_name='update_teacher.html', success_url='/teachers/', id=id)
 
def delete_teacher(request, id):
    return delete_object(request, model=teacher, success_url='/teachers/',id=id)

#books
def book(request):
    return read_objects (request, model=books, template_name='book.html')
def add_books(request):
    return create_object(request, model=books, template_name='add_books.html', success_url='/book/')
def update_book(request,id):
    return update_object(request, model=books, template_name='update_books.html', success_url='/book/', id=id)

def delete_book(request, id):
    return delete_object(request, model=books, success_url='/book/',id=id)
 
#club
def clubs(request):
    return read_objects(request, model=club, template_name='clubs.html')
def add_club(request):
    return create_object(request, model=club, template_name='add_club.html', success_url='/clubs/')
def update_clubs(request,id):
    return update_object(request, model=club, template_name='update_clubs.html', success_url='/clubs/', id=id)
 
def delete_clubs(request, id):
    return delete_object(request, model=club, success_url='/clubs/',id=id)






    


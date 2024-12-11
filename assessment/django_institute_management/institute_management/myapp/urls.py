from django.contrib import admin
from django.urls import path,include
from myapp import views



urlpatterns = [
    path("",views.index),
    path("signup/",views.signup),
    path('login/',views.login,name='login'),
    path('userlogout/',views.userlogout),
    

    path("students/",views.students,name='students'),
    path('add_student/',views.ad_student),
    path('update_students/<int:id>',views.update_students),
    path("delete_student/<int:id>",views.delete_student),

    path('teachers/',views.teachers,name="teachers"),
    path('add_teacher/',views.add_teacher),
    path('update_teacher/<int:id>',views.update_teacher),
    path("delete_teacher/<int:id>",views.delete_teacher),

    path("book/",views.book,name='book'),
    path('add_books/',views.add_books),
    path('update_book/<int:id>',views.update_book),
    path("delete_book/<int:id>",views.delete_book),

    path("clubs/",views.clubs,name="clubs"),
    path('add_club/',views.add_club),
    path('update_clubs/<int:id>',views.update_clubs),
    path("delete_clubs/<int:id>",views.delete_clubs),

]
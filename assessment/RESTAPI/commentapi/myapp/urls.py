from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path("",views.index),
    path("getallcomments/",views.getallcomments),
    path("insertcomments/",views.insertcomments),
    path('updatecomments/<int:id>',views.updatecomments),
    path('deletecomments/<int:id>',views.deletecomments),
]

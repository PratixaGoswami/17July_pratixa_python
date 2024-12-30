from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path("",views.index),
    path("getall/",views.getall),
    path("getbookid/<int:id>/",views.getbookid),
    path("deletebookid/<int:id>/",views.deletebookid),
    path("insertdata/",views.insertdata),
    path("updatebookdata/<int:id>",views.updatebookdata)
]
from django.shortcuts import render
from .models import*
from .forms import*

# Create your views here.
def index(request):
    product= product_mst.objects.all().prefetch_related('product_sub_cat_set')
    return render(request,'index.html',{'product':product})


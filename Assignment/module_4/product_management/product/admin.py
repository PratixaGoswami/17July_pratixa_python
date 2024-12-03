from django.contrib import admin
from .models import*

# Register your models here.
class pro(admin.ModelAdmin):
    list_display=['product_name']


admin.site.register(product_mst, pro)
admin.site.register(product_sub_cat)
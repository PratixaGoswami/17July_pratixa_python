from  rest_framework import serializers
from .models import*

class bookserial(serializers.ModelSerializer):
    class Meta:
        model=book
        fields="__all__" 
        
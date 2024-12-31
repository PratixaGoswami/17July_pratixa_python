from rest_framework import serializers
from .models import*

class comentserializers(serializers.ModelSerializer):
    class Meta:
        model=commentmodel
        fields="__all__"
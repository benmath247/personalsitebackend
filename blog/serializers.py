from rest_framework import serializers
from .models import *

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact 
        fields = ('__all__')

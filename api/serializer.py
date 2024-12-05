from rest_framework import serializers
from .models import programmer , student

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model= programmer 
        #fields= ('fullname', 'nickname', 'age', 'is_active ')
        fields= '__all__'
        
class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'
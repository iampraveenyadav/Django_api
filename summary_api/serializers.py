from rest_framework import serializers 
from .models import UserServicesChtghFinal
 
class UserServicesChtghFinalSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = UserServicesChtghFinal
        fields='__all__'
        #fields = ('id',
                 # 'name')
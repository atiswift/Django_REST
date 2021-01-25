from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','file','date_of_birth')

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password','file','date_of_birth')
        extra_kwargs = {'password':{'write_only':True}}
        # specify arbitrary additional keyword arguments on fields, using the extra_kwargs

    def create(self,validated_data):
        user = User.objects.create_user(validated_data['username'],validated_data['email'],validated_data['password'],validated_data['file'],validated_data['date_of_birth'])
        return user

#to create a user in Django is to use the create_user function. This will handle the hashing of the password, etc..

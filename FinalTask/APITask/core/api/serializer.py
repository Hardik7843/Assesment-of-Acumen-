# from rest_framework import serializer
from rest_framework.serializers import ModelSerializer
from user.models import person
from user.models import company


class PersonSerializer(ModelSerializer):
    class Meta:
        model = person
        fields = '__all__'
        
class CompanySerializer(ModelSerializer):
    class Meta:
        model = company
        fields = '__all__'
    
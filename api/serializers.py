from rest_framework import serializers
from shop.models import Categorial, Product
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class CategorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorial
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
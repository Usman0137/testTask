from rest_framework import serializers
from .models import Cars, CarCategories


class CarCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarCategories
        fields = '__all__'


class CarsSerializer(serializers.ModelSerializer):
    carCategory = CarCategoriesSerializer(read_only=True)

    class Meta:
        model = Cars
        fields = '__all__'

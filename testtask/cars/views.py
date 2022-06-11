from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serilaizers import CarCategoriesSerializer, CarsSerializer
from .models import CarCategories, Cars


class CarsListAPIView(ListCreateAPIView):
    serializer_class = CarsSerializer
    queryset = Cars.objects.all()

    def get_queryset(self):
        return self.queryset.all()


class CarsDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarsSerializer
    queryset = Cars.objects.all()
    lookup_field = 'id'

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.all()


class CarsCategoriesListAPIView(ListCreateAPIView):
    serializer_class = CarCategoriesSerializer
    queryset = CarCategories.objects.all()

    def get_queryset(self):
        return self.queryset.all()


class CarsCategoriesDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarCategories
    queryset = CarCategories.objects.all()
    lookup_field = 'id'

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.all()
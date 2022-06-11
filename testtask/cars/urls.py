from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarsListAPIView.as_view()),
    path('<int:id>', views.CarsDetailAPIView.as_view()),
    path('categories', views.CarsCategoriesListAPIView.as_view()),
    path('category/<int:id>', views.CarsCategoriesDetailAPIView.as_view()),
]
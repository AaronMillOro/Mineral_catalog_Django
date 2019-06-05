from django.urls import path

from . import views

urlpatterns = [
    path('', views.minerals_index, name='minerals_index'),
    path('<int:pk>/', views.mineral_detail, name ='mineral_detail'),
]

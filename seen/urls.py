from django.urls import path
from seen import views

urlpatterns = [
    path('categories/', views.category_list),
    path('categories/<pk>/', views.category_detail)
]

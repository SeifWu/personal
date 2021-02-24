from django.urls import path

from seen import views

urlpatterns = [
    path('categories', views.CategoryList.as_view()),
    path('categories/<pk>', views.CategoryDetail.as_view())
]

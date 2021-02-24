from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from seen import views

urlpatterns = [
    path('categories/', views.category_list),
    path('categories/<pk>/', views.category_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)

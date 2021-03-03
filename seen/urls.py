from django.urls import path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from seen import views
from seen.views import CategoryList, UserViewSet, TagViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'tags', TagViewSet, basename='tag')

urlpatterns = [
    path('categories', CategoryList.as_view()),
    path('categories/<pk>', views.CategoryDetail.as_view())
]

urlpatterns += router.urls

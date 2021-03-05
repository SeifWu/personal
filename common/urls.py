from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from common.views import CustomTokenObtainPairView

urlpatterns = [
    # 登录路由
    path('login', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # 刷新 Token 路由
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]

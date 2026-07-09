from django.urls import path
from .views import RegisterView, LogoutView, PasswordResetRequestView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path('login/refresh/', TokenRefreshView.as_view(), name='login-refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
]
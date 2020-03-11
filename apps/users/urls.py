from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users import views
from .views import registration

urlpatterns = [
    path("register/", registration, name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('profiles/', views.UserProfileList.as_view()),
    path('profiles/<int:pk>/', views.UserProfileDetail.as_view()),
]

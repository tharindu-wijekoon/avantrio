from django.contrib import admin
from django.urls import path
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', CreateUserView.as_view(), name='register')
]

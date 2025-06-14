from django.urls import path
from .views import PublicMessageList, ProtectedMessageList,register_user
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('messages/public/', PublicMessageList.as_view(), name='public-messages'),
    path('messages/protected/', ProtectedMessageList.as_view(), name='protected-messages'),

    # JWT Authentication Endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('register/', register_user, name='register'),

]

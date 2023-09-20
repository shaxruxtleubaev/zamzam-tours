from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    ClientAPIView,
    TourAPIView,
    VideoAPIView,
)

urlpatterns = [
    # Token 
    path('token/', TokenObtainPairView.as_view(), name='token_ontain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Datas
    path('client/', ClientAPIView.as_view(), name='client'),   
    path('tour/', TourAPIView.as_view(), name='tour'),
    path('video/', VideoAPIView.as_view(), name='video')
]
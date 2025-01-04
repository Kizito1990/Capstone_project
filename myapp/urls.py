from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ReviewViewSet, LikeViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'likes', LikeViewSet, basename='like')

urlpatterns = [
            path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
            ] 

urlpatterns += router.urls
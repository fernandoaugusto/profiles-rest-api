from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset') #base_name required because there is no Model for Hello
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login') #base_name required because there is no Model for Login


urlpatterns = [
    url(r'^hello-view/', views.HelloAPIView.as_view()),
    url(r'', include(router.urls))
]

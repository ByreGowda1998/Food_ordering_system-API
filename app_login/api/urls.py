from django.urls import path,include
from app_login.api.views import ContactViewSet,RegistrationViewSet,LogoutViewSet
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token       # ObtainAuthToken is inbuilt from rest_framework where user  logins  using user email and password and genarting token to the user



router = routers.DefaultRouter()
router.register(r'contactus', ContactViewSet,basename="Contact")
router.register(r'register', RegistrationViewSet,basename="Registration")
router.register(r'logout', LogoutViewSet,basename='logout')
urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token),

]
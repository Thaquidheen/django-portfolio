from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.authlogin,name='login'),
    path('registration/',views.authregister,name='registration'),
    path('forget-password/',views.forgetpassword,name='forgetpassword'),
    path('logout/',views.authlogout,name='logout')

]
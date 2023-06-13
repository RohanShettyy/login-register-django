from django.contrib import admin
from django.urls import path, include
from authentication import views
urlpatterns = [
    path('', views.loginpage, name='login'),
    path('signup.html', views.signuppage, name='signup'),
    path('home.html', views.homepage, name='home'),
    path('index.html', views.loginpage, name= 'login'),
    path('signup/registration', views.signuppage, name='registration'),
    path('signup/', views.signuppage, name='signup'),
    path('signup/index.html', views.loginpage, name= 'login'),
    path('reg.html', views.signuppage, name = "reg"),
    path('login/', views.loginpage, name= 'login'),
    path('login/reg.html', views.signuppage, name = "reg"),
    path('login/home.html', views.homepage, name='home'),
    path('login/index.html', views.loginpage, name= 'login'),
    path('logout/', views.logoutuser, name='logout'),
    path('register/', views.register, name = 'register' ),
    path('login/registration.html/', views.register, name = 'register' )

]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.beforeLogin, name="beforeLogin"),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('courses/', views.courses, name="courses"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name='gurukul-about'),
]

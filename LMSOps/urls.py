from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('',views.home,name="home"),
	path('logout/', views.logoutUser, name="logout"),
    path('addbook/',views.addbook,name="addbook"),

]


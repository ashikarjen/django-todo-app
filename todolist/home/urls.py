from django.contrib import admin
from django.urls import path, include
from home import views

admin.site.site_header = "Admin Login For ToDo App"
admin.site.site_title = "Logged in as Admin"
admin.site.index_title = "Welcome to Admin panel"
urlpatterns = [
    path('', views.registration, name='registration'),
    path('login/', views.loginPage, name='loginPage'),
    path('logout/', views.logoutUser, name='logout'),
    path('home/', views.home, name='home'),
    path('tasks', views.tasks, name='tasks')
]
from django.urls import include, path
# from django.contrib import admin
from . import views


urlpatterns = [
	path('dashboard/', views.dashboard, name='dashboard'),
	path('', include('django.contrib.auth.urls')),
	path('register/', views.register, name='register'),
	path('register_done/', views.register_done, name='register_done'),
]
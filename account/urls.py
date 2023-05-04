from django.urls import path
from account import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('activation/<uidb64>/<token>/', views.activation, name='activation'),
    path('reset_password_validate/<uidb64>/<token>/', views.reset_password_validate, name='reset_password_validate'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('reset-password', views.reset_password, name='reset-paasword'),

]
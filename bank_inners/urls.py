from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('analytics/', views.analytics, name='analytics'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('support_agent/', views.support_agent, name='support_agent'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('deposit', views.deposit, name='deposit'),
    path('reg/', views.reg, name='reg'),
    path('reports/', views.reports, name='reports'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('logout/', views.LogoutPage, name='LogoutPage'),
]
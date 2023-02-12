from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.Logout, name='logout'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy')
]
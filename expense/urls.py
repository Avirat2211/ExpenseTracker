from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index,name='index'),
    path("edit/<int:id>/", views.edit,name='edit'),
    path("delete/<int:id>/", views.delete,name='delete'),
    path('login/', auth_views.LoginView.as_view(template_name='expense/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]

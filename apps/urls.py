from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

from apps.views import HomeTemplateView, ProductDetailView, RegisterFormView

urlpatterns = [
    path('home', HomeTemplateView.as_view(), name='home'),
    path('product-detail/<str:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('', LoginView.as_view(template_name='login_registr/login.html'), name='login'),
    path('login', LoginView.as_view(template_name='login_registr/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='login_registr/login.html'), name='logout'),
    path('login_registr',RegisterFormView.as_view(), name='login_registr'),
    path('register', LoginView.as_view(template_name='login_registr/register.html'), name='register'),
    path('profile', views.profile_update, name='profile'),
    path('product', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),

]







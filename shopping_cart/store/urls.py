from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Default route
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('store/', views.store, name='store'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('collections', views.collections, name='collections'),
    path('collections/<str:name>', views.collections_view, name='collections'),
    path('collections/<str:c_name>/<str:p_name>', views.product_details, name='product_details'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('addtocart', views.add_to_cart, name='addtocart'),
]

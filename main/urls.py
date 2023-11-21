from django.urls import path
from . import views
from .views import load_data_view

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('load_data/', load_data_view, name='load_data'),
]

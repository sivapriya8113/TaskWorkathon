from django.urls import path

from . import views
from .api import RegisterApi

urlpatterns=[
    path('api/register/', RegisterApi.as_view()),
    #path('',views.api_overview, name='api_overview'),
    path('product-list/', views.showall, name='product-list'),
    path('product-detail/<int:pk>/', views.Viewproduct, name='product-details'),
    path('product-create/', views.createproduct, name='product-create'),
    path('product-update/<int:pk>/', views.Updateproduct, name='product-update'),
    path('product-delete/<int:pk>/', views.Deleteproduct, name='product-delete'),

]



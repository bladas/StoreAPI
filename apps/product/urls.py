from django.urls import path

from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product-list'),
    path('list/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
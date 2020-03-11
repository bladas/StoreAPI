from django.urls import path

from .views import CartObjectListView

urlpatterns = [
    path('list/', CartObjectListView.as_view(), name='item-list'),
    # path('list/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
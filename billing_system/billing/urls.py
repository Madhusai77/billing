from django.urls import path
from .views import (
    ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView,
    EmployeeListCreateAPIView, EmployeeRetrieveUpdateDestroyAPIView,
    CustomerListCreateAPIView, CustomerRetrieveUpdateDestroyAPIView,
    BillListCreateAPIView, BillRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-destroy'),
    path('employees/', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee-retrieve-update-destroy'),
    path('customers/', CustomerListCreateAPIView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer-retrieve-update-destroy'),
    path('bills/', BillListCreateAPIView.as_view(), name='bill-list-create'),
    path('bills/<int:pk>/', BillRetrieveUpdateDestroyAPIView.as_view(), name='bill-retrieve-update-destroy'),
]

from django.urls import path
from .views import landingview, supplierlistview, productlistview, addsupplier, addproduct, deletesupplier, deleteproduct

urlpatterns = [
    path('', landingview),
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:iidee>/',deletesupplier),
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:iidee>/',deleteproduct),
]
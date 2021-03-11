from django.urls import path
from Order.views import Add_to_Cart,cart_details,cart_delete,OrderCart,OrderForm,OrderProduct,Order



urlpatterns = [
    path('addingcart/<int:id>/', Add_to_Cart, name='Add_to_Cart'),
    path('cart_details/', cart_details, name='cart_details'),
    path('cart_delete/<int:id>/', cart_delete, name='cart_delete'),
    path('order_cart/', OrderCart, name='ordercart'),
    
    
]
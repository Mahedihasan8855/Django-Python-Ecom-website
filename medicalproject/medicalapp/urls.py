from django.urls import path
from .views import Home,product_single,category_product,About,ContactMessage,ContactForm,contact,SearchView

urlpatterns = [
    
    path('',Home,name='home'),
    path('product/<int:id>/', product_single, name='product_single'),
    path('product/<int:id>/<slug:slug>/', category_product, name='category_product'),
    path('about/', About, name='about'),
    path('contact/', contact, name='contact'),
    path('search/', SearchView, name='SearchView'),
    
]


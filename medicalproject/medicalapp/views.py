from django.shortcuts import render,HttpResponse,HttpResponsePermanentRedirect,reverse,HttpResponseRedirect,redirect
from medicalapp.models import ProjectSetting,ContactMessage,ContactForm
from product.models import Product,Images,Category
from medicalapp.forms import SearchForm
from Order.models import Shop_Cart
from django.contrib import messages
# Create your views here.

def Home(request):
    current_user=request.user
    cart_product = Shop_Cart.objects.filter(user_id=current_user.id)
    total_amount=0
    for p in cart_product:
        total_amount+=p.product.new_price*p.quantity
    category=Category.objects.all()
    setting = ProjectSetting.objects.get(id=1)
    sliding_images = Product.objects.all().order_by('id')[:5]
    latest_products = Product.objects.all().order_by('-id')
    products = Product.objects.all()
    
    

    context={'setting':setting,
             'sliding_images':sliding_images,
             'latest_products':latest_products,
             'products':products,
             'category':category,
             'total_amount':total_amount,
             'cart_product':cart_product,
             
    }
    return render(request,'home.html',context)


def product_single(request,id):
    current_user=request.user
    cart_product = Shop_Cart.objects.filter(user_id=current_user.id)
    total_amount=0
    for p in cart_product:
        total_amount+=p.product.new_price*p.quantity
    category = Category.objects.all()
    setting = ProjectSetting.objects.get(id=1)
    single_product=Product.objects.get(id=id)
    images=Images.objects.filter(product_id=id)
    products = Product.objects.all().order_by('id')[:5]
    cart_product = Shop_Cart.objects.filter(user_id=current_user.id)
    context={'setting':setting,
             'single_product':single_product,
             'images':images,
             'products':products,
             'category':category,
             'total_amount':total_amount,
             'cart_product':cart_product,

    }
    return render(request,'product-single.html',context)


def category_product(request,id,slug):
    current_user=request.user
    cart_product = Shop_Cart.objects.filter(user_id=current_user.id)
    total_amount=0
    for p in cart_product:
        total_amount+=p.product.new_price*p.quantity
    category = Category.objects.all()
    setting = ProjectSetting.objects.get(id=1)
    product_cat=Product.objects.filter(category_id=id)
    sliding_images = Product.objects.all().order_by('id')[:5]
    context={'product_cat':product_cat,
             'category': category,
             'setting':setting,
             'sliding_images':sliding_images,
             'total_amount':total_amount,
             'cart_product':cart_product,
    
    }
    return render(request,'category_products.html',context)

def About(request):
    current_user=request.user
    cart_product = Shop_Cart.objects.filter(user_id=current_user.id)
    total_amount=0
    for p in cart_product:
        total_amount+=p.product.new_price*p.quantity
    category = Category.objects.all()
    setting = ProjectSetting.objects.get(id=1)
    context={
             'setting':setting,
             'category':category,
             'total_amount':total_amount,
             'cart_product':cart_product,
             
    
    }
    return render(request,'about.html',context)

def contact(request):
    url=request.META.get('HTTP_REFERER')
    current_user=request.user
    cart_product = Shop_Cart.objects.filter(user_id=current_user.id)
    total_amount=0
    for p in cart_product:
        total_amount+=p.product.new_price*p.quantity
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            data=ContactMessage()
            data.name=form.cleaned_data['name']
            data.email=form.cleaned_data['email']
            data.subject=form.cleaned_data['subject']
            data.message=form.cleaned_data['message']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()

            messages.success(request, '  Your Product Has Been Added Successfully To Cart  ')
            return HttpResponsePermanentRedirect(url)

    setting=ProjectSetting.objects.get(pk=1)
    form=ContactForm
    category = Category.objects.all()
    context={
             'setting':setting,
             'form':form,
             'category':category,
             'total_amount':total_amount,
             'cart_product':cart_product,
    
    }
    
    return render(request,'contact_form.html',context)



def SearchView(request):
    current_user=request.user
    cart_product = Shop_Cart.objects.filter(user_id=current_user.id)
    total_amount=0
    for p in cart_product:
        total_amount+=p.product.new_price*p.quantity
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            cat_id = form.cleaned_data['cat_id']
            if cat_id == 0:
                products = Product.objects.filter(title__icontains=query)
            else:
                products = Product.objects.filter(title__icontains=query, category_id=cat_id)
            category = Category.objects.all()
            sliding_images = Product.objects.all().order_by('id')[:2]
            setting = ProjectSetting.objects.get(pk=1)
            context = {
                'category': category,
                'query': query,
                'product_cat': products,
                'sliding_images': sliding_images,
                'setting': setting,
                'total_amount':total_amount,
                'cart_product':cart_product,
            }
            return render(request, 'searchview.html', context)
    return HttpResponseRedirect('category_product')


def SearchView(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            cat_id = form.cleaned_data['cat_id']
            if cat_id == 0:
                products = Product.objects.filter(title__icontains=query)
            else:
                products = Product.objects.filter(
                    title__icontains=query, category_id=cat_id)
            category = Category.objects.all()
            sliding_images = Product.objects.all().order_by('id')[:2]
            setting = ProjectSetting.objects.get(pk=1)
            context = {
                'category': category,
                'query': query,
                'product_cat': products,
                'sliding_images': sliding_images,
                'setting': setting,
            }
            return render(request, 'category_products.html', context)
    return HttpResponseRedirect('category_product')



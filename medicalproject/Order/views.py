from django.shortcuts import render,HttpResponse,HttpResponsePermanentRedirect,redirect,reverse,HttpResponseRedirect
from product.models import Category,Images,Product
from medicalapp.models import ProjectSetting,ContactMessage,ContactForm
from Order.models import Shop_Cart,OrderForm,OrderProduct,Order,ShoppingCartForm
from django.contrib import messages
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required
from UserApp.models import UserProfile



# Create your views here.
@login_required(login_url='/user/login/')
def Add_to_Cart(request,id):
    url=request.META.get('HTTP_REFERER')
    current_user=request.user
    checking=Shop_Cart.objects.filter(
        product_id=id,user_id=current_user.id
    )
    if checking:
        control=1
    else:
        control=0
    if request.method=="POST":
        form=ShoppingCartForm(request.POST)
        if form.is_valid():
            if control == 1:
                data = Shop_Cart.objects.filter(product_id=id,user_id=current_user.id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else:
                data=Shop_Cart()
                data.user_id = current_user.id
                data.product_id=id
                data.quantity=form.cleaned_data['quantity']
                data.save()
        messages.success(request, '  Your Product Has Been Added Successfully To Cart  ')
        return HttpResponsePermanentRedirect(url)

    else:
        if control==1:
            data=Shop_Cart.objects.filter(product_id=id,user_id=current_user.id)
            data.quantity += 1
            data.save()
        else:
            data=Shop_Cart()
            data.user_id = current_user
            data.product_id=id
            data.quantity=1
            data.save()
        return HttpResponsePermanentRedirect(url)
            

def cart_details(request):
    current_user=request.user
    category = Category.objects.all()
    setting = ProjectSetting.objects.get(id=1)
    images=Images.objects.all()
    cart_product = Shop_Cart.objects.filter(user_id=current_user.id)
    total_amount=0
    for p in cart_product:
        total_amount+=p.product.new_price*p.quantity

    
    context={'setting':setting,
             'images':images,
             'cart_product':cart_product,
             'category':category,
             'total_amount':total_amount,

    }
    
    return render(request,'cart_details.html',context)

def cart_delete(request,id):
    url=request.META.get('HTTP_REFERER')
    current_user=request.user
    cart_product = Shop_Cart.objects.filter(id=id,user_id=current_user.id)
    cart_product.delete()
    messages.warning(request, '  Your Product Has Been Removed Successfully From The Cart  ')
    return HttpResponseRedirect(url)


@login_required(login_url='/user/login/')
def OrderCart(request):
    current_user=request.user
    shopping_cart=Shop_Cart.objects.filter(user_id=current_user.id)
    totalamount=0
    for rs in shopping_cart:
        totalamount += rs.quantity*rs.product.new_price
    if request.method == "POST":
        form=OrderForm(request.POST,request.FILES)
        if form.is_valid():
            dat = Order()
            # get product quantity from form
            dat.first_name = form.cleaned_data['first_name']
            dat.last_name = form.cleaned_data['last_name']
            dat.address = form.cleaned_data['address']
            dat.city = form.cleaned_data['city']
            dat.phone = form.cleaned_data['phone']
            dat.country = form.cleaned_data['country']
            dat.transaction_id = form.cleaned_data['transaction_id']
            dat.transaction_image = form.cleaned_data['transaction_image']
            dat.user_id = current_user.id
            dat.total = totalamount
            dat.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(5).upper()  # random code generator
            dat.code = ordercode
            dat.save()

            for rs in shopping_cart:
                data = OrderProduct()
                data.order_id = dat.id
                data.product_id = rs.product_id
                data.user_id = current_user.id
                data.quantity = rs.quantity
                data.price = rs.product.new_price
                data.amount = rs.amount
                data.save()
                product = Product.objects.get(id=rs.product_id)
                product.amount -= rs.quantity
                product.save()


            Shop_Cart.objects.filter(user_id=current_user.id).delete()
            messages.success(request, 'Your order has been completed')
            category = Category.objects.all()
            setting = ProjectSetting.objects.get(id=1)
            context = {
                
                'ordercode': ordercode,
                'category': category,
                'setting': setting,
            }
            return render(request, 'order_completed.html', context)
        else:
            messages.warning(request, form.errors)

    form = OrderForm()
    profile = UserProfile.objects.get(user_id=current_user.id)
    total_amount = 0
    for p in shopping_cart:
        total_amount += p.product.new_price*p.quantity
    category = Category.objects.all()
    setting = ProjectSetting.objects.get(id=1)

    context = {
        'category':category,
        'shoping_cart': shopping_cart,
        'totalamount': totalamount,
        'profile': profile,
        'form': form,
        'category': category,
        'setting': setting,
        'total_amount': total_amount
    }
    messages.warning(request, form.errors)
    return render(request, 'order_form.html', context)
        

           

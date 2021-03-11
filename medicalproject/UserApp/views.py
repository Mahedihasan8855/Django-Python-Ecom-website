from django.shortcuts import render,redirect,HttpResponsePermanentRedirect
from django.contrib.auth import logout,login,authenticate,update_session_auth_hash
from product.models import Category
from django.contrib import messages
from medicalapp.models import ProjectSetting
from UserApp.forms import SignupForm,UserUpdateForm,ProfileUpdateForm
from UserApp.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.

def user_login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, '" You Have Successfully Logged in to Mr. Pharmacy"')
            return redirect('home')
            
        else:
            messages.error(request, '  Your username or password is invalid.. Please Try Again..! ')
    category = Category.objects.all()
    setting = ProjectSetting.objects.get(id=1)
    context={
        'category':category,
        'setting':setting,
    }
    return render(request,'user_login.html',context)


def user_logout(request):
    logout(request)
    messages.error(request, '  "You Have Successfully Logged Out From Mr. Pharmacy "')
    return redirect('home')



def user_register(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password)
            login(request,user)
            current_user=request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.image="user_img/downloaded.jpg"
            data.save()
            messages.info(request, '" You Have Successfully Registered an Account in Mr. Pharmacy"')
            return redirect('home')
        else:
            messages.error(request, '  Something went wrong...! Please try again...   ')

    else:
        form=SignupForm()
    category = Category.objects.all()
    setting = ProjectSetting.objects.get(id=1)
    context={
        'category':category,
        'setting':setting,
        'form':form,
    }
    return render(request,'user_register.html',context)


def user_profile(request):
    category = Category.objects.all()
    setting = ProjectSetting.objects.get(id=1)
    current_user=request.user
    profile=UserProfile.objects.get(user_id=current_user.id)
    context={
        'category':category,
        'setting':setting,
        'profile':profile,
    }
    return render(request,'user_profile.html',context)

@login_required(login_url='/user/login')
def user_update(request):
    if request.method=='POST':
        user_form=UserUpdateForm(request.POST,instance=request.user)
        profile_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, '" Your account has been updated successfully"')
            return redirect('user_profile')

    else:
        user_form=UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=request.user)
        category = Category.objects.all()
        setting = ProjectSetting.objects.get(id=1)


        context={
        'user_form':user_form,
        'profile_form':profile_form,
        'category':category,
        'setting':setting,
                
        }
        return render(request,'user_update.html',context)


@login_required(login_url='/user/login')
def user_password(request):
    if request.method=='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request, '" Your password has been changed successfully"')
            return redirect('user_profile')
        else:
            messages.error(request, '" Please correct the error below."<br>'+str(form.errors))
            return redirect('user_password')
    else:
        category = Category.objects.all()
        setting = ProjectSetting.objects.get(id=1)
        form=PasswordChangeForm(request.user)
        context={
        'form':form,
        'category':category,
        'setting':setting,
                
        }
        return render(request,'userpasswordupdate.html',context)

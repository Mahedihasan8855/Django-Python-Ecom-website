from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.forms import ModelForm, TextInput, EmailInput
from django import forms


# Create your models here.


class ProjectSetting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),)
    
    title =models.CharField(max_length=200)
    keyword=models.CharField(max_length=200)
    description=models.TextField()
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=18)
    fax=models.CharField(blank=True,max_length=50)
    email=models.EmailField(blank=True,null=True,max_length=100)
    smptserver=models.CharField(max_length=100)
    smptemail=models.EmailField(blank=True,null=True,max_length=100)
    smptpassword=models.CharField(blank=True,max_length=50)
    smptport=models.CharField(blank=True,max_length=150)
    icon=models.ImageField(blank=True,null=True,upload_to='icon/')
    about_icon=models.ImageField(blank=True,null=True,upload_to='icon/')
    facebook=models.CharField(blank=True,max_length=100)
    instagram=models.CharField(blank=True,max_length=100)
    address=models.TextField()
    contact=models.TextField()
    reference=models.TextField()
    status=models.CharField(max_length=50,choices=STATUS)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),)
    name=models.CharField(max_length=180)
    email=models.EmailField(max_length=80)
    subject=models.CharField(max_length=200, blank=True)
    message=models.TextField(max_length=1000,blank=True)
    status=models.CharField(max_length=50,choices=STATUS,default='New')
    ip=models.CharField(max_length=100,blank=True)
    note=models.CharField(max_length=200,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class ContactForm(ModelForm):
    class Meta:
        model=ContactMessage
        fields=['name','email','subject','message']
        widgets={
            'name':TextInput(attrs={'class':'input','placeholder':'Name & Surname'}),
            'email':EmailInput(attrs={'class':'input','placeholder':'write your email'}),
            'subject':TextInput(attrs={'class':'input','placeholder':'write your subject'}),
            'message':TextInput(attrs={'class':'input','placeholder':'write your message'}),

        }



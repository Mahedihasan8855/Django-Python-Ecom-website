from django.urls import path
from UserApp.views import user_logout,user_login,user_register,user_profile,user_update,user_password


urlpatterns = [
    
    
    path('logout/',user_logout,name='user_logout'),
    path('login/',user_login,name='user_login'),
    path('register/',user_register,name='user_register'),
    path('profile/',user_profile,name='user_profile'),
    path('user_update/',user_update,name='user_update'),
    path('user_password/',user_password,name='user_password'),
    
]
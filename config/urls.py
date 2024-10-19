"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from app.views import  base, watch, Login, Logout, category, Watches_list, Register, Users, update_user, UserRegister, ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('category/<int:cat_id>/', category, name='category'),
    path('base/', base, name='base'),
    path('', watch, name='watch'),
    path('watches_list/', Watches_list.as_view(), name='watches_list'),
    path('register/', Register.as_view(), name='register'),
    path('users/', Users.as_view(), name='users'),
    path('user-register/', UserRegister.as_view(), name='user_register'),
    path('update-user/<int:id>/', update_user, name='update_user'),
    path('profile/', ProfileView.as_view(), name='profile')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

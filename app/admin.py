from django.contrib import admin

from .models import User, Category, Watch, Karzinka

admin.site.register([User, Category, Watch, Karzinka])
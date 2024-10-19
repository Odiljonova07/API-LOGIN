from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import User, Category, Watch, Karzinka
from .forms import LoginForm, RegisterForm, UpdateForm

class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.user_role == 'admin':
                    return redirect('base')
                elif user.user_role == 'xaridor':
                    return redirect('watch')
                
            return render(request, 'login.html', {'form': form})

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')
    

class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', context={"form":form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('base')
        return render(request, 'register.html', context={"form":form})
    
class UserRegister(View):
    def get(self, request):
        form = RegisterForm()
        categories = Category.objects.all()
        return render(request, 'user_register.html', context={"form":form, "categories":categories})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('watch')
        return render(request, 'user_register.html', context={"form":form})


class Users(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'users.html', context={"users":users})


def update_user(request, id):
    user = get_object_or_404(User, id=id)
    form = UpdateForm(instance=user)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    return render(request, 'update_user.html', context={"form":form})    


class ProfileView(View):
    def get(self, request):
        return render(request, 'profile.html')

    

class Watches_list(View):
    def get(self, request):
        watches = Watch.objects.all()
        return render(request, 'watches_list.html', context={"watches":watches})
    

def category(request, cat_id):
    category = get_object_or_404(Category, id=cat_id)
    watches = category.watches.all()
    categories = Category.objects.all()
    return render(request, 'watch.html', context={"watches":watches, "categories":categories})


def base(request):
    return render(request, 'base.html')


def watch(request):
    categories = Category.objects.all()
    watches = Watch.objects.all()
    karzinka = Karzinka.objects.count()
    return render(request, 'watch.html', context={"categories":categories, "watches":watches, "karzinka":karzinka})
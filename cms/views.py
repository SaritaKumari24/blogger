from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

from django.views.generic import FormView,ListView,View,CreateView
from django.contrib.auth.hashers import make_password
from .models import *
# Create your views here.

class PostList(ListView):
    model=BloggerPost
    template_name = 'home.html'
    queryset = BloggerPost.objects.filter(status=1)



class LoginView(FormView):
    template_name="login.html"
    form_class=AuthenticationForm
    success_url='/'

    def post(self,r):
        username=r.POST.get('username')
        password=r.POST.get('password')

        user=authenticate(username=username,password=password)

        if user is not None:
            if user.is_active:
                login(r,user)
                return redirect('home')
            else:
                return HttpResponse("INACTIVE USER")
        else:
            return HttpResponse('INVALID USER')
            
class LogoutView(View):
    def get(self,r):
        logout(r)
        return redirect("login") 

class RegisterView(CreateView):
    model=User
    fields=['first_name','last_name','username','password','email']
    template_name="register.html"
    success_url="/login/"

    def form_valid(self, form):
        user=form.save(commit=False)

        user.password=make_password(user.password)
        user.save()
        return super().form_valid(form)                 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from  . import forms
from  django.views.generic import FormView
from  . import models as user_models


class LoginView(FormView):
    template_name="login.html"
    form_class=forms.LoginForm

    def form_valid(self, form):
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        user=authenticate(self.request,username=email, password=password)

        if user is not None:
            login(self.request, user)

            return render(self.request, 'home.html')
        return super().form_vaild(form)

class SignUpView(FormView):
    template_name="signup.html"
    form_class=forms.SignUpform

    def form_valid(self,form):
        form.save()
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        user=authenticate(self.request, username=email,password=password)
        if user is not None:
            login(self.request, user)

            return render(self.request, 'home.html')
        super(SignUpView,self).form_valid(form)

#로그아웃함수입니다. 필요시 사용하면 좋을것 같아 만들었습니다.
def Logout(request):

    logout(request)
    
    return redirect('home')

def privacy_policy(request):
    return render(request, 'privacy-policy.html')
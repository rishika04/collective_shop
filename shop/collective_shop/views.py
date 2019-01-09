# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django import forms
from django.conf import settings
from django.contrib.auth import update_session_auth_hash, authenticate, login, logout, forms as auth_forms
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def index(request):
    return render(request, 'collective_shop/index.html')

class UserCreateForm(auth_forms.UserCreationForm):
    first_name = forms.RegexField(label=_("Name"), max_length=30, regex=r'^[a-z A-Z]{2,30}$',
            help_text=_("Required. 30 characters or fewer. Letters, digits, spaces and dots(.) only."),
            error_messages={'invalid': _("This value may contain only letters.")})
    last_name = forms.RegexField(label=_("Name"), max_length=30, regex=r'^[a-z A-Z]{2,30}$',
            help_text=_("Required. 30 characters or fewer. Letters, digits, spaces and dots(.) only."),
            error_messages={'invalid': _("This value may contain only letters.")})
    email = forms.EmailField()

    # class Meta:
    #     model = User
    #     fields = ("username", "email", "first_name", "last_name" ,"password1", "password2")

    def save(self, datas, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.is_active = True
        user.save()
        return user

@sensitive_post_parameters('password1')
@csrf_protect
@csrf_exempt
def signup(request):
    #if request.user.is_authenticated():
      #  return redirect(reverse('dashboard'))

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        phone = request.POST.get('phone')
        form = UserCreateForm({
            'first_name': first_name,
            'last_name': last_name, 
            'username': email, 
            'email': email, 
            'password1': password,
            'password2': password,
            })
        if form.is_valid():
            datas = dict()
            datas['username'] = form.cleaned_data['email']
            datas['email'] = form.cleaned_data['email']
            datas['password1'] = form.cleaned_data['password1']
            user = form.save(datas)

          
            return render(request, 'collective_shop/dashboard.html')
    else:
        form = UserCreateForm()
    return render(request, 'collective_shop/signup.html', {'form': form})


def signin(request):
    # if request.user.is_authenticated():
    #     return redirect(reverse('dashboard'))
    # next=""
    # error = ""
    if request.GET:
		next = request.GET.get('next')
	
    form = auth_forms.AuthenticationForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            active = Activation.objects.get(user=user)	
            if user and active.is_validated:
                login(request, user)
                if not next:
                    return redirect(reverse('services'))
                return redirect(next)
            


    return render(request, 'collective_shop/signin.html', {'form': form})


@login_required(login_url=settings.LOGIN_URL)
def signout(request):
    logout(request)
    return redirect('/')

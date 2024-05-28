from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginUsersForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

class LoginUser(LoginView):
    form_class = LoginUsersForm
    template_name = 'users/login.html'
    extra_context = {'tetle': 'авторизация'}

    # def get_success_url(self) -> str:
    #     return reverse_lazy('index')

# def login_user(request):
#     if request.method == 'POST':
#         form = LoginUsersForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'],
#                                  password=cd['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#     else:
#         form = LoginUsersForm()

#     return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))

def register_user(request):
    return HttpResponse('register')
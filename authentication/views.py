# from django.contrib.auth import authenticate, login, logout
# from django.shortcuts import render, redirect
# from . import forms
# from django.views.generic import View


# def login_page(request):
#     form = forms.LoginForm()
#     message = ''
#     if request.method == 'POST':
#         form = forms.LoginForm(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password']
#             )
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 message = 'Login failed! '
#     return render(request,
#                   'authentication/login.html',
#                   context={'form': form, 'message': message})

# class LoginPageView(View):
#     template_name = 'authentication/login.html'
#     form_class = forms.LoginForm
#
#     def get(self, request):
#         form = self.form_class()
#         message = ''
#         return render(request,
#                       'authentication/login.html',
#                       context={'form': form, 'message': message})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#         message = ''
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password']
#             )
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 message = 'Login failed! '
#
#         return render(request,
#                       'authentication/login.html',
#                       context={'form': form, 'message': message})


# def logout_user(request):
#     logout(request)
#     return redirect('login')

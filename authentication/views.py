from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from . import forms
# from django.views.generic import View


def signup_page(request):
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, 'authentication/signup.html',
                  context={'form': form})


def upload_profile_photo(request):
    form = forms.UploadProfilePhotoForm()
    if request.method == 'POST':
        form = forms.UploadProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'authentication/upload_profile_photo.html',
                  context={'form': form})


def follow_users(request):
    form = forms.FollowUsersForm(instance=request.user)
    if request.method == 'POST':
        form = forms.FollowUsersForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,
                  'authentication/follow_users.html',
                  context={'form': form})


# # Login function-based view
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

# # Login class-based view
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

# # Logout function-based view
# def logout_user(request):
#     logout(request)
#     return redirect('login')

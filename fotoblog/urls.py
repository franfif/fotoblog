from django.contrib import admin
from django.contrib.auth.views import LoginView, \
    LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path

import authentication.views
# import authentication.views
import blog.views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', authentication.views.LoginPageView.as_view(), name='login'),
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True,
    ), name='login'),
    # path('logout/', authentication.views.logout_user, name='logout'),
    path('logout/', LogoutView.as_view(
        template_name='authentication/logout.html',
    ), name='logout'),
    path('home/', blog.views.HomePageView.as_view(), name='home'),
    path('password-change/', PasswordChangeView.as_view(
        template_name='authentication/password_change.html',
    ), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html',
    ), name='password_change_done'),
    path('signup/', authentication.views.signup_page, name='signup'),
]

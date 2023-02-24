from django.conf import settings
from django.conf.urls.static import static
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
    path('profile_photo/', authentication.views.upload_profile_photo, name='upload_profile_photo'),
    # path('logout/', authentication.views.logout_user, name='logout'),
    path('logout/', LogoutView.as_view(
        template_name='authentication/logout.html',
    ), name='logout'),
    path('password-change/', PasswordChangeView.as_view(
        template_name='authentication/password_change.html',
    ), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html',
    ), name='password_change_done'),
    path('signup/', authentication.views.signup_page, name='signup'),

    path('home/', blog.views.home_page, name='home'),
    path('home/<int:user_id>/', blog.views.home_page, name='home'),
    path('blog/photo_upload/', blog.views.photo_upload, name='photo_upload'),
    path('blog/new_blog/', blog.views.photo_and_blog_upload, name='blog_photo_upload'),
    path('blog/<int:blog_id>/', blog.views.view_blog, name='view_blog'),
    path('blog/<int:blog_id>/edit/', blog.views.edit_blog, name='edit_blog'),
    path('blog/<int:blog_id>/delete/', blog.views.confirm_delete_blog, name='delete_blog'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

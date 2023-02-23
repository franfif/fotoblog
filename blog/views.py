from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# from django.views.generic import View
# from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms, models


@login_required
def home_page(request, user_id=None):
    if user_id:
        photos = models.Photo.objects.filter(uploader=user_id)
    else:
        photos = models.Photo.objects.all()
    return render(request, 'blog/home.html', context={'photos': photos})

# class HomePageView(LoginRequiredMixin, View):
#     template_name = 'blog/home.html'
#     login_url = ''
#     # redirect_field_name = 'redirect_to'

    # def get(self, request):
    #     return render(request, self.template_name)


def photo_upload(request):
    form = forms.PhotoForm()
    if request.method == 'POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect('home')
    return render(request, 'blog/photo_upload.html', context={'form': form})

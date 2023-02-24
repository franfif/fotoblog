from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# from django.views.generic import View
# from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms, models


@login_required
def home_page(request, user_id=None):
    if user_id:
        photos = models.Photo.objects.filter(uploader=user_id)
        blogs = models.Blog.objects.filter(author=user_id)
    else:
        photos = models.Photo.objects.all()
        blogs = models.Blog.objects.all()

    return render(request,
                  'blog/home.html',
                  context={'photos': photos,
                           'blogs': blogs})


# class HomePageView(LoginRequiredMixin, View):
#     template_name = 'blog/home.html'
#     login_url = ''
#     # redirect_field_name = 'redirect_to'

    # def get(self, request):
    #     return render(request, self.template_name)


@login_required
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


@login_required
def photo_and_blog_upload(request):
    photo_form = forms.PhotoForm()
    blog_form = forms.BlogForm()
    if request.method == 'POST':
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        blog_form = forms.BlogForm(request.POST)
        if all([photo_form.is_valid(), blog_form.is_valid()]):
            photo = photo_form.save(commit=False)
            blog = blog_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            blog.author = request.user
            blog.photo = photo
            blog.save()
            return redirect('home')

    return render(request,
                  'blog/photo_blog_upload.html',
                  context={'photo_form': photo_form,
                           'blog_form': blog_form})


@login_required
def view_blog(request, blog_id):
    blog = models.Blog.objects.get(id=blog_id)
    return render(request,
                  'blog/view_blog.html',
                  context={'blog': blog})

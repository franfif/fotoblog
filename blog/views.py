from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.forms import formset_factory
from django.shortcuts import render, redirect, get_object_or_404
# from django.views.generic import View
# from django.contrib.auth.mixins import LoginRequiredMixin
from itertools import chain
from . import forms, models


@login_required
def home_page(request, user_id=None):
    if user_id:
        blogs = models.Blog.objects.filter(contributors__id=user_id)
        photos = models.Photo.objects.filter(uploader=user_id)
        blogs_and_photos = sorted(chain(blogs, photos),
                                  key=lambda x: x.date_created,
                                  reverse=True)
    else:
        blogs = models.Blog.objects.filter(
            Q(contributors__in=request.user.follows.all()) |
            Q(starred=True))
        photos = models.Photo.objects.filter(uploader__in=request.user.follows.all()).exclude(blog__in=blogs)
        blogs_and_photos = sorted(chain(blogs, photos),
                                  key=lambda x: x.date_created,
                                  reverse=True)
    return render(request,
                  'blog/home.html',
                  context={'blogs_and_photos': blogs_and_photos})


def photo_feed(request):
    photos = models.Photo.objects.filter(uploader__in=request.user.follows.all()).order_by('-date_created')
    return render(request,
                  'blog/photo_feed.html',
                  context={'photos': photos})

# class HomePageView(LoginRequiredMixin, View):
#     template_name = 'blog/home.html'
#     login_url = ''
#     # redirect_field_name = 'redirect_to'

    # def get(self, request):
    #     return render(request, self.template_name)


@login_required
@permission_required('blog.add_photo', raise_exception=True)
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
@permission_required('blog.add_blog', raise_exception=True)
def photo_and_blog_upload(request):
    photo_form = forms.PhotoForm()
    blog_form = forms.BlogForm()
    if request.method == 'POST':
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        blog_form = forms.BlogForm(request.POST)
        if all([photo_form.is_valid(), blog_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            blog = blog_form.save(commit=False)
            # blog.author = request.user
            blog.photo = photo
            blog.save()
            blog.contributors.add(request.user,
                                  through_defaults={'contribution': 'Primary author'})
            return redirect('home')

    return render(request,
                  'blog/photo_blog_upload.html',
                  context={'photo_form': photo_form,
                           'blog_form': blog_form})


@login_required
def view_blog(request, blog_id):
    blog = get_object_or_404(models.Blog, id=blog_id)
    return render(request,
                  'blog/view_blog.html',
                  context={'blog': blog})


@login_required
@permission_required('blog.change_blog', raise_exception=True)
def edit_blog(request, blog_id):
    blog = get_object_or_404(models.Blog, id=blog_id)
    edit_form = forms.BlogForm(instance=blog)
    delete_form = forms.DeleteBlogForm()
    if request.method == 'POST':
        if 'edit_blog' in request.POST:
            edit_form = forms.BlogForm(request.POST, instance=blog)
            if edit_form.is_valid():
                blog = edit_form.save()
                blog.contributors.add(request.user)
                return redirect('view_blog', blog_id)
        if 'delete_blog' in request.POST:
            return redirect('delete_blog', blog_id)
    return render(request,
                  'blog/edit_blog.html',
                  context={'edit_form': edit_form,
                           'delete_form': delete_form})


@login_required
@permission_required('blog.delete_blog', raise_exception=True)
def confirm_delete_blog(request, blog_id):
    blog = get_object_or_404(models.Blog, id=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('home')
    return render(request,
                  'blog/delete_blog.html',
                  context={'blog': blog})


@login_required
@permission_required('blog.add_photo', raise_exception=True)
def create_multiple_photos(request):
    PhotoFormset = formset_factory(forms.PhotoForm, extra=5)
    formset = PhotoFormset()
    if request.method == 'POST':
        formset = PhotoFormset(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    photo = form.save(commit=False)
                    photo.uploader = request.user
                    photo.save()
            return redirect('home')
    return render(request,
                  'blog/create_multiple_photos.html',
                  context={'formset': formset})

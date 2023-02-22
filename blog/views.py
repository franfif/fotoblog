# from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


# @login_required
# def home_page(request):
#     return render(request, 'blog/home.html')

class HomePageView(LoginRequiredMixin, View):
    template_name = 'blog/home.html'
    login_url = ''
    # redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, self.template_name)

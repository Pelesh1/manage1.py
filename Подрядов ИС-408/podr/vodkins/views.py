from django.shortcuts import render
from django.views import View

from django.http import HttpResponseRedirect


class log(View):
    def get(self, request):
        context = {}
        return render(request, 'regestration.html', context=context)


class MainPage(View):
    def get(self, request):
        context = {}
        return render(request, 'index.html', context=context)

# Create your views here.

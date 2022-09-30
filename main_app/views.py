from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class Home(View):
    def get(self, request):
        return HttpResponse('Budget Home')

class About(View):
    def get(self, request):
        return HttpResponse('Budget About')

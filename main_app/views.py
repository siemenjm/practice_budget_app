from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

# Add Institution Class for mock data
class Institution:
    def __init__(self, institution_id, name, logo):
        self.institution_id = institution_id
        self.name = name
        self.logo = logo

# Fake Institution Data
institutions = [
    Institution('ins_1', 'Chase Bank', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtaSOK8ycH6cN56fkzGoyUW30utQ71XiGx0Q&usqp=CAU'),
    Institution('ins_2', 'Bank of America', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZ57oF7N_QozC50QZCwHL_UhoNBxbw-Ldlgg&usqp=CAU'),
    Institution('ins_3', 'PNC Bank', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjPq4L0RWsvCEIXJcvMJHurh4eyC03y2VTpQ&usqp=CAU')
]

class InstitutionList(TemplateView):
    template_name = 'institution_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["institutions"] = institutions # this is where we add the key into our context object for the view to use
        return context

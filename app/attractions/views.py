from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Attraction

class AttractionListView(ListView):
    template_name = 'attraction_list.html'
    model = Attraction

class AttractionDetailView(DetailView):
    template_name = 'attraction_detail.html'
    model = Attraction

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['added_breadcrumbs'] = [{'url':self.object.get_absolute_url, 'title':self.object.title}]
        context['page_title'] = self.object.title
        return context
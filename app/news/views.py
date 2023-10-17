from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    template_name = 'news/post_list.html'
    model = Post
    paginate_by = 12

class PostDetailView(DetailView):
    template_name = 'news/post_detail.html'
    slug_field = 'alias'
    model = Post

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['added_breadcrumbs'] = [{'url':self.object.get_absolute_url, 'title':self.object.title}]
        images = self.object.imagepost_set.all()
        videos = self.object.videopost_set.all()
        context['main_image'] = images[0] if images else None
        context['main_video'] = videos[0] if videos else None
        context['images'] = images[1:] if len(images) > 1 else None
        context['videos'] = videos[1:] if len(videos) > 1 else None
        context['page_title'] = self.object.title
        return context
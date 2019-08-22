from django.shortcuts import render

# Create your views here.
# C R U D I

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .models import Bookmark

class BookmarkList(ListView):
    model = Bookmark

from django.urls import reverse_lazy

class BookmarkCreate(CreateView):
    model = Bookmark
    fields = ['site_name','url','description']
    success_url = reverse_lazy('bookmark_list')

class BookmarkUpdate(UpdateView):
    model = Bookmark
    fields = ['description']
    success_url = reverse_lazy('bookmark_list')


class BookmarkDelete(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark_list')
   # template_name_suffix = "_delete"
    template_name_suffix = '_delete'

class BookmarkDetail(DetailView):
    model = Bookmark
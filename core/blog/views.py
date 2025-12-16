from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from .models import Post
from .forms import CreatePost
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

"""
 Create class based view
"""
class IndexViews(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context
    

class RedirectToMaktab(RedirectView):
    url = 'https://maktabkhooneh.com'

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)
    

class ListPost(ListView):
    context_object_name = 'posts'
    paginate_by = 2
    model = Post
    ordering = '-id'

    # def get_queryset(self):
        # posts = Post.objects.all()
        # return posts


class DetailPostView(DetailView):
    model = Post
    
    

'''
class CreatePostView(FormView):
    template_name = 'create-post.html'
    form_class = CreatePost
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
'''

class PostCreateView(CreateView):
    model = Post
    form_class = CreatePost
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(UpdateView):
    model = Post
    form_class = CreatePost
    success_url = '/blog/post/'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/blog/post/'



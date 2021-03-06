from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q

from rest_framework import viewsets

from .models import Post
from analytics.models import View
from .serializers import PostSerializer


# Create your views here.

def home(request):
    search_query = request.GET.get('q', None) # Get the search query or if it doesn't exist then set the query to None.
    print(request)
    print(request.GET)
    print(request.GET.get('q'))
    posts = Post.objects.all()
    if search_query:
        post_list = posts.filter(
            Q(title__icontains=search_query) | \
            Q(content__icontains=search_query) | \
            Q(author__username__istartswith=search_query)
        )
        post_list.order_by('date_posted')
    else:
        post_list = posts
    context = {
        'posts':post_list,
        }
    return render(request, 'blog/home.html', context=context) 


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = "posts"

    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

    def get_object(self):
        post_pk = self.kwargs.get("pk")
        if post_pk:
            post_query = Post.objects.filter(pk=post_pk) # model.objects returns a list
            if post_query.exists():
                post_object = post_query.first() # Grab the first (and only) obj in list
                view, created = View.objects.get_or_create(
                    post = post_object,
                )
                if view:
                    view.views_count += 1
                    view.save()
                return post_object
        raise Http404


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

####### API DEVELOPMENT #######

class PostViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('date_posted')
    serializer_class = PostSerializer

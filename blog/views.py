# Third party  imports.
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)
from django.shortcuts import render
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView,
)

# Local application import
from .models import Post


def home(request):
    """
       Homepage view which lists all the posts in 
       the database.
    """
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    """
       View for listing all posts.
    """
    model = Post
    template_name = 'blog/home.html' 
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    """
        View for a post's details
    """
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """
       View for creating a new post.
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
        View for Updating a post.
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """
            Assigns the post to the current author.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
            UserPassesTextMixin checks if it is the user before allowing
            him/her to update a post.
        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
        View for deleting a post.
    """
    model = Post
    success_url = '/'

    def test_func(self):
        """
            UserPassesTextMixin checks if it is the user before allowing
            him/her to delete post.
        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    """
        View for about page.
    """
    context = {'title': 'About'}
    template_name = 'blog/about.html'
    return render(request, template_name, context)

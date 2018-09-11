from django.shortcuts import render
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView,
)
from .models import Post


# View for listing all posts.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    """View for listing all posts.
    """
    model = Post
    template_name = 'blog/home.html' 
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    """View for a post's details
    """
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """View for creating a new post.
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """View for Updating a post.
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # UserPassesTextMixin checks if it is the user before allowing
    # him/her to update a post.
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """View for deleting a post.
    """
    model = Post
    success_url = '/'

    # UserPassesTextMixin checks if it is the user before allowing
    # him/her to delete post.
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# View for about page.
def about(request):
    context = {'title': 'About'}
    template_name = 'blog/about.html'
    return render(request, template_name, context)

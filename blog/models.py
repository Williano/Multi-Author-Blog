from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    """Creates Model for a post in the database.
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Display a post with the title at the admin backend.
    def __str__(self):
        return self.title

    # Creates the absolute url for a particular post.
    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.pk})

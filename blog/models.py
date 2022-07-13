from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from blog.misc import RATING_TYPE, OK


class AbstractTopic(models.Model):
    category = models.CharField(max_length=255, default='')
    date_created = models.DateTimeField(auto_now_add=True, auto_created=True)

    class Meta:
        abstract = True


class Topic(AbstractTopic):
    name = models.CharField(max_length=255, default="", null=False, blank=False)
    title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}-{self.id}"

    def get_absolute_url(self):
        return reverse("topics")


class Post(models.Model):
    topic = models.ForeignKey(Topic, related_name="posts", on_delete=models.CASCADE)
    text = models.TextField()
    name = models.CharField(max_length=255)
    likes_count = models.IntegerField(default=0)
    beauty_content = RichTextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}-{self.id}"

    def get_absolute_url(self):
        return reverse("posts", kwargs={'pk': self.topic.id})


class AbstractComment(models.Model):
    owner_name = models.CharField(max_length=255, default='')
    date_created = models.DateTimeField(auto_now_add=True, auto_created=True)

    class Meta:
        abstract = True


class Comment(AbstractComment):
    post = models.ForeignKey(Post, related_name="comment", on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(choices=RATING_TYPE, default=OK)

    def __str__(self):
        return f"{self.text}-{self.id}"

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.post.id})

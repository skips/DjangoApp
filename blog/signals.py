from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Post


@receiver(post_save, sender=Post)
def my_handler(sender, instance, **kwargs):
    for comment in instance.comment.all():
        if comment.rating < 3:
            comment.delete()

from django.db import models

from django.utils import timezone

class Post(models.Model):
    author = models.CharField(max_length=100)
    body = models.TextField(default="helo")
    created_at    = models.DateTimeField(editable=False,auto_now_add=True)
    updated_at   = models.DateTimeField(blank=True,auto_now_add=True)
    title = models.CharField(max_length=100)
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.updated_at = timezone.now()
        return super(Post, self).save(*args, **kwargs)

from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=False)
    # content = models.TextField()
    content = RichTextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' ' + self.content + ' ' + str(self.date_created) + ' ' + str(self.date_updated)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.content + ' ' + str(self.date_created) + ' ' + str(self.post)
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    thumbnail = models.ImageField(default="413065110.jpg",blank=True)
    input_by = models.ForeignKey(User, default=None,on_delete = models.DO_NOTHING)
    def __str__(self):
        return self.title
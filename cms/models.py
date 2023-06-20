from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.


class Category(models.Model):
    cat_title = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.cat_title
    

class Post(models.Model):
    title = models.CharField(max_length=200,unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image = models.ImageField(upload_to="post/")
    slug = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
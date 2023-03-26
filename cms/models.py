from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

STATUS=(
    (0,'Draft'),
    (1,'Publish')
)
class BloggerPost(models.Model):
    title=models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug=models.SlugField(max_length=200)
    image=models.ImageField()
    description=models.TextField()
    update_on=models.DateTimeField(auto_now=True)
    status=models.IntegerField(choices=STATUS, default=0)
    
    def __str__(self):
        return self.title
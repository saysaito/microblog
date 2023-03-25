from django.db import models
class Post(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    intro=models.TextField()
    body=models.TextField()
    posted_date=models.DateTimeField(auto_now_add=True)
    tags=models.ManyToManyField('Tag',blank=True,related_name='posts')
# Create your models here.
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=80)
    email=models.EmailField()
    body=models.TextField()
    posted_date=models.DateTimeField(auto_now_add=True)

class Tag(models.Model):

    name=models.CharField(max_length=50)
    slug=models.SlugField()
    def __str__(self):
        return self.name



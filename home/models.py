from distutils.command.upload import upload
from statistics import mode
from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    # tags
    slug = models.SlugField(null=True,blank=True) #To be used later
    image = models.ImageField(upload_to = 'media/notes/',null=True,blank=True) #To be used lateer
    github_link = models.CharField(max_length= 100,blank=True)
    # To collect Step Details
    json_steps = models.TextField(default="[]",blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
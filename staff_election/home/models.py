from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class posts(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
class candidates(models.Model):
    name = models.CharField(max_length=100)
    post = models.ForeignKey(posts, verbose_name=_("Post"), on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class booths(models.Model):
    name = models.CharField(max_length=100)
    submitted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
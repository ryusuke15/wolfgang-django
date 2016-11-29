from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    message = models.TextField()
    received  = models.DateTimeField(auto_now=False, auto_now_add = True)

    def __unicode__(self):
        return self.name

class Video_link(models.Model):
    title = models.CharField(max_length=120)
    videoId = models.CharField(max_length=120)
    def __unicode__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.FileField()
    link = models.URLField()
    created = models.DateTimeField(auto_now=False, auto_now_add = True)

    def __unicode__(self):
        return self.name
            
    def admin_image(self):
        return '<img style="width:120px;height:120px;"src="/media/%s"/>' % self.image
    admin_image.allow_tags = True

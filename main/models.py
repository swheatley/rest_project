from django.db import models


class Phone(models.Model):
    age = models.IntegerField(null=True, blank=True) 
    slug = models.SlugField(null=True, blank=True)
    images = models.CharField(null=True, blank=True, max_length=255)
    name = models.CharField(max_length=255, null=True, blank=True)
    snippet = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

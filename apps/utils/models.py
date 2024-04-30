from django.db import models


class Base(models.Model):
    """Base model for apps"""
    
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['created_on']

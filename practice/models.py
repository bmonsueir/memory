from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime

class English(models.Model):
    word = models.CharField(max_length = 255)
    definition = models.CharField( max_length=255, )
  
    def __str__(self):
        return self.word 
  
class German(models.Model):
    english = models.ForeignKey(English, on_delete=models.CASCADE)
    word = models.CharField(max_length = 255)
    definition = models.CharField( max_length=255, )
  
    def __str__(self):
        return self.word 
        
class Spanish(models.Model):
    english = models.ForeignKey(English, on_delete=models.CASCADE)
    word = models.CharField(max_length = 255)
    definition = models.CharField( max_length=255, )
  
    def __str__(self):
        return self.word 
        
class Russian(models.Model):
    english = models.ForeignKey(English, on_delete=models.CASCADE)
    word = models.CharField(max_length = 255)
    definition = models.CharField( max_length=255, )
  
    def __str__(self):
        return self.word 
   
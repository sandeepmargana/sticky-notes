from django.db import models

# Create your models here.
class Note(models.Model):
    note_txt = models.TextField()
    color = models.CharField(max_length=10 , default="#ccffcc")
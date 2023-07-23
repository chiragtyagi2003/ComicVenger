from django.db import models

# Create your models here.

class MakeStory(models.Model):
    
    # fields in table
    prompt = models.TextField()
    story = models.TextField()

    def __str__(self):
        return self.prompt
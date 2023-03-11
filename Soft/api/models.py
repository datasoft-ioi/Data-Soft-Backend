from django.db import models

class Base(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()


    def __str__(self) -> str:
        return self.title
    

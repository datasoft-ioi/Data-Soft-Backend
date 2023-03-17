from django.db import models

# FAQ model 
class Base(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()


    def __str__(self) -> str:
        return self.title
    

# About page
class About(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()

    def __str__(self) -> str:
        return self.title


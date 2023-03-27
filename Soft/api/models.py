from django.db import models

# FAQ model 
class Base(models.Model):

    # uzb
    title = models.CharField(max_length=200)
    desc = models.TextField()

    # rus
    rus_title = models.CharField(max_length=200)
    rus_desc = models.TextField(max_length=200)



    def __str__(self) -> str:
        return self.title
    

# About page
class About(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()


    def __str__(self) -> str:
        return self.title


# Gallery
class Gallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/galley/%Y/%m/%d')

    def __str__(self) -> str:
        return self.title
    

# OurProjects
class OurProjects(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/%Y/%m/%d')
    url = models.CharField(max_length=200)


# Asosiy sayt uchun
class HomeTitle(models.Model):
    uz_title = models.CharField(max_length=200)
    ru_title = models.CharField(max_length=200)

    uz_mini_desc = models.CharField(max_length=200)
    ru_mini_desc = models.CharField(max_length=200)

    def __str__(self):
        return self.uz_title
    


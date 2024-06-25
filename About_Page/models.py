from django.db import models

# Create your models here.
class Page_Settings(models.Model):
    page_Title = models.CharField(max_length=20)
    section_Title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')
    vision = models.CharField(max_length=400)
    def __str__(self):
        return self.page_Title
class Core_Values(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    def __str__(self):
        return self.title
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class InsightsCategory(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
class Insights(models.Model):
    category = models.ForeignKey(InsightsCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    cover_photo = models.ImageField(upload_to='insights/')
    author = models.CharField(max_length=50)
    author_profile = models.ImageField(upload_to='insights/author/') 
    desc = RichTextField()
    timestamp = models.DateField(auto_now=True)
    @property
    def get_short_desc(self):
        return self.desc[:130]
    def __str__(self):
        return self.title
class FutureWork(models.Model):
    title = models.CharField(max_length=80)
    cover_photo = models.ImageField(upload_to='insights/')
    desc = models.TextField()
    def __str__(self):
        return self.title
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Title(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name
class Image(models.Model):
    name = models.CharField(max_length=20)
    background = models.ImageField(upload_to='background/')
    def __str__(self):
        return self.name
class Service(models.Model):
    title = models.CharField(max_length=60)
    icon = models.FileField(upload_to='icon/')
    banner = models.FileField(upload_to='service/')
    description = models.TextField()
    serve = models.TextField()
    long_Description = RichTextField()
    def __str__(self):
        return self.title
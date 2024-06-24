from django.db import models

# Create your models here.
class Setting(models.Model):
    site_Name = models.CharField(max_length=30)
    logo = models.FileField(upload_to='logo/')
    favicon = models.FileField(upload_to='favicon/')
    year = models.IntegerField()
    address = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)
    youtube = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    abn = models.CharField(max_length=40)
    description = models.TextField()
    def __str__(self):
        return self.site_Name
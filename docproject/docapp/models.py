from django.db import models

# Create your models here.
class Document(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    year=models.TextField()
    img=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name

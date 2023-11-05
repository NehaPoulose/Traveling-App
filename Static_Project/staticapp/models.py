from django.db import models

# Create your models here.
class fastservices(models.Model):
    name = models.CharField(max_length = 250)
    image = models.ImageField(upload_to = 'pics')
    description = models.TextField()


    def __str__(self):
        return self.name


class teammembers(models.Model):
    name1 = models.CharField(max_length = 250)
    image1 = models.ImageField(upload_to = 'photos')
    description1 = models.TextField()

    def __str__(self):
        return self.name1
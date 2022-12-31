from django.db import models

class MyhpModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class ImageUpload(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/')#こちらの通り

    def __str__(self):
        return self.title





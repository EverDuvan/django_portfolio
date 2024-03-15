from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    date = models.DateField( auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    read_only_fields = ['created_at', 'updated_at']

    def __str__(self):
        return self.title
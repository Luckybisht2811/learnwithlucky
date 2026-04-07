from django.db import models
from cloudinary.models import CloudinaryField

LANGUAGE_CHOICES = [
    ('Python', 'Python'),
    ('C', 'C Language'),
    ('Django', 'Django'),
    ('Java', 'Java'),
]

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video = CloudinaryField('video', resource_type='video')
    thumbnail = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.title


class Note(models.Model):
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES, default='Python')
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = CloudinaryField('file', resource_type='raw')

    def __str__(self):
        return self.title
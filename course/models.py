from django.db import models

LANGUAGE_CHOICES = [
    ('Python', 'Python'),
    ('C', 'C Language'),
    ('Django', 'Django'),
    ('Java', 'Java'),
]

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video = models.FileField(upload_to='course_videos/')
    thumbnail = models.ImageField(upload_to='course_thumbnails/', blank=True, null=True)

    def __str__(self):
        return self.title


class Note(models.Model):
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES, default='Python')
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='notes/')

    def __str__(self):
        return self.title
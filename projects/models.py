from django.db import models

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='projects/')
    repository = models.URLField(blank=True, null=True)
    skills = models.ManyToManyField(Skill)
    
    def __str__(self):
        return self.name
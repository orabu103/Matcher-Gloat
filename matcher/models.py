from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Title(models.Model):
    name = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return f'ID:{self.id} Name:{self.name}'

class Skill(models.Model):
    name = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return f'ID:{self.id} Name:{self.name}'
    

class Candidate(models.Model):
    title = models.ForeignKey(Title , on_delete=models.CASCADE)
    skill = models.ManyToManyField(Skill)

    def __str__(self):
        return f'ID:{self.id} Title:{self.title}'
    
    
class Job(models.Model):
    title = models.ForeignKey(Title , on_delete=models.CASCADE)
    skill = models.ManyToManyField(Skill)

    def __str__(self):
        return f'ID:{self.id} Title:{self.title}'
    
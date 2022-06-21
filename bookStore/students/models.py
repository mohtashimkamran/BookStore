from django.db import models

# Create your models here.

class Student(models.Model):
    roll_number = models.IntegerField(primary_key=True,null=False,blank=False)
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
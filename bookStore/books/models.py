from django.db import models 
from adminView.models import User


# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=255)
    listed_by = models.ForeignKey(User, editable=False, null=True, blank=True, on_delete= models.PROTECT)
    status = models.BooleanField(default=False, verbose_name='is_active')


    def __str__(self) -> str:
        return self.name
from django.db import models

# Create your models here.
class Dojo(models.Model):
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
class Ninja(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    dojo=models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.SET_NULL, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
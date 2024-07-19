from django.db import models

# Create your models here.
class company(models.Model):
    name = models.TextField(unique=True)

class person(models.Model):
    uniqe_id = models.TextField(max_length=30)
    email = models.TextField(max_length=30)
    url = models.TextField()
    # company = models.ForeignKey(company , on_delete=models.CASCADE  )


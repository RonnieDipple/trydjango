from django.db import models

# Create your models here.
# Whenever you make changes run python3 manage.py makemigrations, python3 manage.py migrate

class Product(models.Model):
    title = models.CharField(max_length=120) # max = required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(blank=False, null=False)#Blank is false meaning filling text is required, if null can be empty in the database
    featured = models.BooleanField()# can say null = True, default= True or both for all these fields


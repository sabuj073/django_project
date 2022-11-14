from django.db import models

# Create your models here.
class Post(models.Model):
    user_name = models.CharField(max_length=300)
    user_email = models.CharField(max_length=300)
    user_zipcode = models.CharField(max_length=300)
    user_city = models.CharField(max_length=300)
    user_state = models.CharField(max_length=300)
    user_address = models.CharField(max_length=300)
    html_format = models.CharField(max_length=300)
    plain_text = models.CharField(max_length=300)
    
    
class Form_DATA(models.Model):
    user_name = models.CharField(max_length=300)
    user_email = models.CharField(max_length=300)
    user_zipcode = models.CharField(max_length=300)
    user_city = models.CharField(max_length=300)
    user_state = models.CharField(max_length=300)
    user_address = models.CharField(max_length=300)
    html_format = models.CharField(max_length=300)
    plain_text = models.CharField(max_length=300)
    
class Form_DATA_NEW(models.Model):
    user_name = models.CharField(max_length=300)
    user_email = models.CharField(max_length=300)
    user_zipcode = models.CharField(max_length=300)
    user_city = models.CharField(max_length=300)
    user_state = models.CharField(max_length=300)
    user_address = models.CharField(max_length=300)
    html_format = models.CharField(max_length=300)
    plain_text = models.CharField(max_length=300)
    
    
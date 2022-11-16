from django.db import models


    
    
class FORM_DATA_FROM_USERS(models.Model):
    user_name = models.CharField(max_length=300)
    user_email = models.CharField(max_length=300)
    user_zipcode = models.CharField(max_length=300)
    user_city = models.CharField(max_length=300)
    user_state = models.CharField(max_length=300)
    user_address = models.CharField(max_length=300)
    mobile_number = models.CharField(max_length=300)
    whatsapp_number = models.CharField(max_length=300)
    distributor = models.CharField(max_length=300)
    counter_type = models.CharField(max_length=300)
    electricity_consumption = models.CharField(max_length=300)
    surface_ownership = models.CharField(max_length=300)
    type_of_roof = models.CharField(max_length=300)
    user_interest = models.CharField(max_length=300)
    
    
    
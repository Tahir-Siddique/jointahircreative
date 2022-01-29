from django.db import models
from django.forms import DateField
import random
import string
# Create your models here.

class UserRecord(models.Model):
    Selling_Key = models.CharField(max_length=1000,blank=True,null=True)
    Order_Revenue_Date = models.DateField(auto_now=True, auto_now_add=False)
    Funds_Cleared_Date = models.DateField(auto_now=True, auto_now_add=False)
    From = models.CharField(max_length=50)
    Percentage_For_Tahir = models.FloatField()
    Percentage_For_Sohail = models.FloatField()
    Total_Price = models.FloatField()
    Getting_Price = models.FloatField()
    Is_Blocked = models.BooleanField("Is Blocked")


    def save(self, *args, **kwargs):
        self.Selling_Key = self.WithoutRepeat(26)
        print(self.Selling_Key)
        super(UserRecord, self).save(*args, **kwargs)
    def WithoutRepeat(self,length):  
        letters = string.ascii_lowercase # define the specific string  
        # define the condition for random.sample() method  
        result = ''.join((random.sample(letters, length)))   
        return result 
    def __str__(self):
        return self.From